# BOT DE WHATSAPP – AUTOMATIZACIÓN Y DETECCIÓN DE RESPUESTAS

Hola, profesor Andrés:

A continuación encontrará las instrucciones para instalar, configurar y ejecutar el bot de WhatsApp desarrollado en Python.

El proyecto utiliza **Python y Playwright** para automatizar la interacción con WhatsApp Web, enviar mensajes de prueba y detectar cuándo el destinatario responde, permitiendo finalizar automáticamente el ciclo de envío.

## 1. Requisitos previos

Antes de iniciar, es necesario tener instalados los siguientes programas:

- Python 3.13 o una versión compatible.
- Visual Studio Code (recomendado).
- Google Chrome o Chromium.
- Git.
- Conexión a Internet.
- Una cuenta de WhatsApp activa.

## 2. Descargar el proyecto

Clonar el repositorio desde GitHub:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto:

```bash
cd python_blucle
```

## 3. Crear el entorno virtual

Ejecutar el siguiente comando:

```bash
py -m venv venv
```

## 4. Activar el entorno virtual

En Windows CMD:

```cmd
venv\Scripts\activate
```

En PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Si aparece un error relacionado con la política de ejecución en PowerShell, se puede utilizar CMD para activar el entorno virtual.

## 5. Instalar las dependencias

Actualizar pip:

```bash
python -m pip install --upgrade pip
```

Instalar Playwright:

```bash
pip install playwright
```

Instalar el navegador Chromium utilizado por Playwright:

```bash
python -m playwright install chromium
```

## 6. Ejecutar el bot

Una vez instaladas las dependencias y activado el entorno virtual, ejecutar:

```bash
python bot.py
```

Si el archivo se encuentra en otra ubicación, se debe utilizar la ruta correspondiente.

## 7. Configuración inicial de WhatsApp

1. Ejecutar el programa.
2. Se abrirá una ventana del navegador.
3. Ingresar a WhatsApp Web si todavía no hay una sesión iniciada.
4. Presionar ENTER en la terminal cuando WhatsApp esté listo.
5. El programa abrirá la conversación configurada.
6. Comenzará el proceso de automatización.

## 8. Funcionamiento del bot

El bot está diseñado para realizar las siguientes operaciones:

- Enviar mensajes automáticamente con un intervalo de 10 segundos.
- Comprobar si existen respuestas nuevas cada 5 segundos.
- Identificar mensajes entrantes y diferenciarlos de los mensajes enviados por el usuario.
- Finalizar el ciclo de envío cuando detecta una respuesta nueva.
- Cerrar el navegador al terminar la ejecución.

La detección de mensajes recibidos utiliza los elementos de WhatsApp Web identificados durante las pruebas con Playwright.

## 9. Estructura recomendada del proyecto

```text
python_blucle/
│
├── bot.py
├── README.md
├── requirements.txt
├── .gitignore
└── venv/
```

El entorno virtual y los archivos de sesión de WhatsApp no deben publicarse en GitHub.

## 10. Detener el programa

Para detener manualmente la ejecución, utilizar:

```bash
CTRL + C
```

El programa también finaliza automáticamente cuando detecta una respuesta entrante nueva.

## 11. Consideraciones importantes

- Mantener una conexión estable a Internet.
- No cerrar WhatsApp Web mientras el bot está funcionando.
- No compartir públicamente los datos de acceso ni las sesiones de WhatsApp.
- Utilizar la automatización únicamente con destinatarios que hayan aceptado recibir los mensajes.
- Los selectores de WhatsApp Web pueden cambiar con sus actualizaciones, por lo que podría ser necesario adaptar el detector.

---

**Atentamente,**

**Jefferson Alfonso**

Gracias, profesor Andrés.