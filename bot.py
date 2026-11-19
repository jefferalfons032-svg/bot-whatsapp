
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# =====================================================
# CONFIGURACIÓN ORIGINAL
# =====================================================

USER_DATA_DIR = "./whatsapp_session"
PHONE_NUMBER = "573214120927"

MESSAGE = (
    "Soy un bot de prueba fabricado por el mejor profe, "
    "este mensaje se enviará automáticamente cada 10 segundos "
    "hasta que el destinatario responda. "
    "¡Gracias por tu paciencia!"
)

INTERVAL_SECONDS = 10
CHECK_FREQUENCY = 5


# =====================================================
# OBTENER MENSAJES RECIBIDOS
# =====================================================

def obtener_mensajes_recibidos(page):

    resultado = page.locator(
        '[data-testid="msg-container"]'
    )

    recibidos = set()

    for i in range(resultado.count()):

        mensaje = resultado.nth(i)

        # Los mensajes entrantes tienen tail-in.
        if mensaje.locator(
            '[data-testid="tail-in"]'
        ).count() == 0:
            continue

        contenido = mensaje.locator(
            '.copyable-text'
        ).first

        if contenido.count() == 0:
            continue

        identificador = contenido.get_attribute(
            "data-pre-plain-text"
        )

        if not identificador:
            continue

        texto = mensaje.inner_text()

        recibidos.add((identificador, texto))

    return recibidos


# =====================================================
# ESPERAR Y DETECTAR RESPUESTAS NUEVAS
# =====================================================

def comprobar_respuesta(page, mensajes_iniciales):

    actuales = obtener_mensajes_recibidos(page)

    nuevos = actuales - mensajes_iniciales

    if nuevos:

        print("\n================================")
        print("¡RESPUESTA RECIBIDA!")
        print("================================")

        for identificador, texto in nuevos:
            print("\nMensaje recibido:")
            print(texto)

        return True

    return False


# =====================================================
# EJECUTAR BOT
# =====================================================

def ejecutar_bot():

    with sync_playwright() as p:

        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False
        )

        try:

            page = (
                context.pages[0]
                if context.pages
                else context.new_page()
            )

            print("Abriendo WhatsApp Web...")

            page.goto("https://web.whatsapp.com")

            input(
                "Abre WhatsApp y presiona ENTER cuando esté listo..."
            )

            page.goto(
                f"https://web.whatsapp.com/send?phone={PHONE_NUMBER}"
            )

            caja_mensaje = page.locator(
                'footer div[contenteditable="true"]'
            ).first

            caja_mensaje.wait_for(timeout=60000)

            print("\nConversación abierta correctamente.")

            # =================================================
            # CARGAR HISTORIAL ANTES DE INICIAR
            # =================================================

            print("\nEsperando que WhatsApp cargue los mensajes...")

            mensajes_iniciales = obtener_mensajes_recibidos(page)

            conteo_anterior = -1
            estable = 0

            while estable < 5:

                actuales = obtener_mensajes_recibidos(page)

                if len(actuales) == conteo_anterior:
                    estable += 1
                else:
                    estable = 0

                conteo_anterior = len(actuales)

                print(
                    f"\rHistorial: {len(actuales)} mensajes | "
                    f"Estabilidad: {estable}/5",
                    end="",
                    flush=True
                )

                time.sleep(1)

            # Tomar una nueva referencia cuando el historial
            # haya terminado de estabilizarse.
            mensajes_iniciales = obtener_mensajes_recibidos(page)

            print("\n\nHistorial cargado correctamente.")
            print(
                "Mensajes recibidos existentes:",
                len(mensajes_iniciales)
            )

            # =================================================
            # BUCLE ORIGINAL DE ENVÍO
            # =================================================

            numero_envios = 0

            print("\nIniciando bot...")
            print("Esperando respuestas nuevas.\n")

            while True:

                # Comprobar antes de enviar.
                if comprobar_respuesta(page, mensajes_iniciales):
                    break

                # Enviar mensaje.
                caja_mensaje.fill(MESSAGE)
                caja_mensaje.press("Enter")

                numero_envios += 1

                print(
                    f"\nMensaje número {numero_envios} enviado."
                )

                # Esperar 10 segundos y revisar cada 5.
                tiempo_transcurrido = 0

                while tiempo_transcurrido < INTERVAL_SECONDS:

                    tiempo_espera = min(
                        CHECK_FREQUENCY,
                        INTERVAL_SECONDS - tiempo_transcurrido
                    )

                    time.sleep(tiempo_espera)

                    tiempo_transcurrido += tiempo_espera

                    print(
                        f"\nComprobando respuesta... "
                        f"{tiempo_transcurrido}s"
                    )

                    if comprobar_respuesta(
                        page,
                        mensajes_iniciales
                    ):
                        break

                else:
                    continue

                # Si se detectó una respuesta, terminar.
                break

            print("\n================================")
            print("BOT FINALIZADO CORRECTAMENTE")
            print("No se enviarán más mensajes.")
            print("================================")

        except KeyboardInterrupt:

            print("\nBot detenido manualmente.")

        except PlaywrightTimeoutError:

            print("\nNo se pudo cargar la conversación a tiempo.")

        except Exception as error:

            print("\nSe produjo un error:")
            print(error)

        finally:

            context.close()
            print("\nWhatsApp Web cerrado.")


if __name__ == "__main__":
    ejecutar_bot()
