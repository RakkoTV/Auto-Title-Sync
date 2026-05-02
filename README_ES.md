# Auto-Title-Sync para OBS Studio

Actualiza automáticamente el título de tu stream basado en el juego/aplicación que estás transmitiendo, con soporte multiplataforma para Twitch y YouTube.

![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Licencia](https://img.shields.io/badge/licencia-MIT-green)
![OBS](https://img.shields.io/badge/OBS-28.0%2B-orange)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## Características

- **Detección Automática de Juego**: Detecta automáticamente la ventana del juego/aplicación actual
- **Multiplataforma**: Actualiza títulos en Twitch y YouTube simultáneamente
- **Rotación de Títulos**: Cicla entre múltiples títulos en un horario
- **Contador de Espectadores**: Incluye el conteo actual de espectadores en el título
- **Plantillas Personalizadas**: Usa placeholders como `{game}`, `{title}`, `{viewers}`, `{time}`
- **UI Multilingüe**: Español, Inglés, Japonés, Chino
- **Atajos de Teclado**: Actualiza el título instantáneamente con un atajo

## Instalación

1. Descarga [`auto_title_sync.py`](auto_title_sync.py)
2. En OBS Studio, ve a **Herramientas → Scripts**
3. Clic en el botón "+" y selecciona el archivo descargado
4. Configura tus credenciales en las propiedades del script

## Configuración

### Paso 1: Obtener Credenciales de Twitch

1. Ve a [Consola de Desarrolladores de Twitch](https://dev.twitch.tv/console)
2. Crea una nueva aplicación
3. Copia tu **Client ID**
4. Genera un **Token OAuth** con el alcance `channel:manage:broadcast`

### Paso 2: Obtener Credenciales de YouTube

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea credenciales OAuth 2.0
3. Habilita YouTube Data API v3
4. Copia tu **API Key** y **Channel ID**

### Paso 3: Configurar el Script

| Configuración | Descripción | Predeterminado |
|--------------|-------------|----------------|
| Habilitar Twitch | Actualizar título de stream de Twitch | Apagado |
| Client ID | Client ID de aplicación de Twitch | - |
| Token OAuth | Token OAuth de Twitch con permisos | - |
| ID de Canal | Tu ID de usuario de Twitch | - |
| Habilitar YouTube | Actualizar título de stream de YouTube | Apagado |
| Detectar Juego | Detectar automáticamente juego/ventana actual | Encendido |
| Incluir Espectadores | Agregar conteo de espectadores al título | Apagado |
| Intervalo de Actualización | Frecuencia de actualización (segundos) | 60 |
| Rotar Títulos | Ciclar entre múltiples títulos | Apagado |
| Intervalo de Rotación | Tiempo entre rotaciones de título (minutos) | 30 |

### Plantillas de Título

Usa estos placeholders en tus títulos:

- `{game}` - Nombre del juego/aplicación actual
- `{title}` - Título original del stream
- `{viewers}` - Conteo actual de espectadores
- `{time}` - Hora actual (formato HH:MM)

Ejemplo: `Jugando {game} | {viewers} espectadores`

### Atajos de Teclado

- **Ctrl+Shift+T** (predeterminado): Actualizar título de stream inmediatamente

## Requisitos

- **OBS Studio**: 28.0 o superior
- **Python**: 3.8 o superior (incluido con OBS)
- **Sistema Operativo**: Windows 10+, macOS 12+, Linux

## Solución de Problemas

**Problema**: El script no aparece en OBS
- **Solución**: Asegúrate de que Python esté instalado y OBS esté actualizado

**Problema**: El título no se actualiza en Twitch
- **Solución**: Verifica que tu token OAuth tenga el alcance `channel:manage:broadcast`

**Problema**: La detección de juegos no funciona
- **Solución**: La detección de juegos actualmente funciona solo en Windows. Linux/macOS próximamente

## Registro de Cambios

### Versión 1.0.0 (2026-05-01)
- Lanzamiento inicial
- Integración con Twitch y YouTube
- Detección automática de juegos
- Rotación de títulos
- Soporte multilingüe

## Soporte

- Issues: [GitHub Issues](https://github.com/RakkoTV/Auto-Title-Sync/issues)
- Discusiones: [GitHub Discussions](https://github.com/RakkoTV/Auto-Title-Sync/discussions)

## Donar

Si encuentras útil este proyecto, por favor considera apoyar el desarrollo:

[![Donar](https://img.shields.io/badge/PayPal-Donar-blue)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&currency_code=USD)

**[Donar vía PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&currency_code=USD)**

## Conéctate Conmigo

- **[GitHub](https://github.com/RakkoTV)** - ⭐ 3 Estrellas
- **[LinkedIn](https://www.linkedin.com/in/ramiro-silva/)** - 👥 449 Contactos
- **[Instagram](https://www.instagram.com/Rakko.Tech)** - 👥 6666 Seguidores
- **[Twitch](https://www.twitch.tv/RakkoTech)** - 👥 8800 Seguidores
- **[X/Twitter](https://www.x.com/RakkoTech)** - 👥 245 Seguidores

## Licencia

Este proyecto está licenciado bajo Licencia MIT - ver [LICENSE](LICENSE) para detalles.

## Agradecimientos

- Equipo de OBS Studio por la increíble plataforma de streaming
- Equipos de API de Twitch y YouTube

---

Hecho con ❤️ por [RakkoTV](https://github.com/RakkoTV)
