# Guía de Contribución 🤝

¡Bienvenido! Para participar en este taller, sigue estos pasos:

## 📜 Pasos para Contribuir

1. **Haz un Fork**: Crea tu copia del repositorio central.
2. **Clona tu copia localmente**: 
   ```bash
   git clone https://github.com/TU-USUARIO/practica-fork-pr.git
   ```
3. **Crea una nueva rama**: Sigue las convenciones de GitFlow (`feature/tu-nombre`):
   ```bash
   git checkout -b feature/mi-termino
   ```
4. **Agrega tu término en `diccionario.json`**:
   - Abre `diccionario.json` y añade un nuevo objeto al final de la lista.
   - **Formato:**
     ```json
     {
       "termino": "Tu Término",
       "definicion": "Tu Definición",
       "autor": "Tu Nombre"
     }
     ```
5. **Prueba tu cambio**: Ejecuta `python main.py` para verificar que tu término aparece correctamente.
6. **Haz commit de tus cambios**:
   ```bash
   git add .
   git commit -m "feat: agrega término [tu-termino]"
   ```
7. **Sube tus cambios a tu fork**:
   ```bash
   git push origin feature/mi-termino
   ```
8. **Crea un Pull Request**: Ve al repositorio original y verás la opción "Compare & Pull Request". ¡Listo!

## 💡 Reglas del taller

- Un término por Pull Request.
- No borres los términos de tus compañeros.
- Verifica el formato JSON (comas, llaves, etc.).
- Sé creativo y descriptivo con la definición.

¡Feliz codificación! 🚀
