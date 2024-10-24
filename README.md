**API REST sencilla con Django y Django REST Framework**

Esta es una API REST sencilla creada con Django y Django REST Framework.

Para probar esta API, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Jeidev26/mi-primera-api-rest.git 

2.  **Crea un entorno virtual y actívalo (opcional pero recomendado)**: Una vez descargado, ingresa desde una terminal a la ruta del directorio raíz e instala **`virtualenv`**:
    
    **bash**
    

    
    **`pip install virtualenv`** 
    
    Luego, ejecuta **`virtualenv venv`** para crear la carpeta **`venv`**. Por último, activa el entorno virtual:
    
    **bash**
    
    
    **venv\Scripts\activate  # En Windows**
    
    **source venv/bin/activate  # En macOS/Linux`** 
    
    Deberías ver algo como esto: **`(venv) C:\Users\Pepito\Desktop\Repo_clonado>`**
    
3.  **Instala las dependencias**: Debes instalar las dependencias necesarias:
    
    **bash**
    

    
    **`pip install django`**
   **`pip install djangorestframework`** 
    
4.  **Inicia el servidor**:
    
    **bash**
    

    
    **`python manage.py runserver`** 
    

Ahora, tu API estará corriendo localmente. Puedes interactuar con ella mediante herramientas como [Postman](https://www.postman.com/) o [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client).

**Nota**: Este proyecto está diseñado para probarse localmente y no está desplegado en Render ni en ningún otro servicio en este momento.
