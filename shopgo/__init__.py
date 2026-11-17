import sys
from pathlib import Path

# Agrega la raíz del proyecto (Apellido_Nombre_QA/) al path para poder hacer `import shopgo`
RAIZ = Path(__file__).resolve().parent.parent
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))