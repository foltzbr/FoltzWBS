# Foltz WBS 🔔

![Python](https://img.shields.io/badge/Python-3-blue) ![Requests](https://img.shields.io/badge/requests-2.32-green) ![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Termux-orange) ![License](https://img.shields.io/badge/license-MIT-yellow)

**Foltz WBS** es una herramienta interactiva en Python para gestionar y usar webhooks de forma eficiente: añadir, listar, verificar y eliminar webhooks, además de enviar mensajes masivos a los webhooks configurados.

**Idioma:** [Português](README.pt.md) • [English](README.md) • Español (este archivo)

## Contenido

- [Funciones](#funciones)
- [Requisitos](#requisitos)
- [Estructura](#estructura)
- [Primeros pasos](#primeros-pasos)
- [Cómo usar](#cómo-usar)
- [Personalización](#personalización)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Funciones

- Añadir nuevos webhooks
- Eliminar webhooks existentes
- Listar todos los webhooks guardados
- Verificar que los webhooks funcionan
- Enviar mensajes masivos a los webhooks
- Banners ASCII personalizables
- Efecto de máquina de escribir en la terminal

## Requisitos

- **Python 3.x** instalado
- **pip** para instalar las dependencias (`colored`, `requests`)

## Estructura

```
FoltzWBS/
├── LICENSE
├── README.md
└── foltz-wbs/
    ├── main.py                  # script principal (menú interactivo)
    ├── requirements.txt         # dependencias (colored, requests)
    ├── install_requirements.bat # instala las dependencias (Windows)
    ├── start.bat                # inicia el programa (Windows)
    ├── webhooks.txt             # webhooks guardados
    └── ascii_banners/           # banners personalizables
```

## Primeros pasos

Sigue estos pasos para instalar y usar Foltz WBS en tu sistema.

### Instalación

#### Windows

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   ```

2. **Instala las dependencias:**

   Ejecuta el archivo `install_requirements.bat`:

   ```bash
   install_requirements.bat
   ```

3. **Inicia el script:**

   Ejecuta el archivo `start.bat`:

   ```bash
   start.bat
   ```

#### Linux

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   ```

2. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta el script:**

   ```bash
   python main.py
   ```

#### Termux

1. **Instala Python y Git:**

   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```

2. **Clona el repositorio e instala las dependencias:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   pip install -r requirements.txt
   ```

3. **Ejecuta el script:**

   ```bash
   python main.py
   ```

## Cómo usar

1. **Inicia Foltz WBS.**
2. **Elige una opción del menú:**
   - **Añadir Webhook**: añade una nueva URL de webhook (se guarda en `webhooks.txt`).
   - **Eliminar Webhook**: elimina un webhook existente.
   - **Listar Webhooks**: ve todos los webhooks guardados.
   - **Verificar Webhooks**: comprueba que los webhooks funcionan.
   - **Enviar Mensajes**: envía mensajes masivos a los webhooks.

## Archivos `.bat`

- **`install_requirements.bat`**: instala las librerías necesarias (`colored`, `requests`).
- **`start.bat`**: inicia el script principal.

## Personalización

- **Banners**: personaliza los banners editando los archivos en `ascii_banners/`.
- **Efecto de texto**: ajusta el efecto de máquina de escribir en el script como quieras.

## Licencia

Este proyecto está bajo la MIT License. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Dudas o sugerencias:

- **Foltz** - [GitHub](https://github.com/foltzbr)
