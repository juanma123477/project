# project

## Cómo publicar esta app

### Despliegue rápido

1. Sube este repositorio a GitHub.
2. Crea una cuenta en Render, Railway, o Fly.
3. Crea un nuevo servicio web y conecta tu repo.
4. Estas plataformas usarán `requirements.txt` y `Procfile`.
5. Publica y copia la URL pública que te entreguen.

### Ejecución local

```bash
python app.py
```

### Archivos creados

- `requirements.txt`: Flask y Gunicorn.
- `Procfile`: instrucción para ejecutar `gunicorn app:app`.
