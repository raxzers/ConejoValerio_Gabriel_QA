## Instalación del ambiente virual
dentro de  VScode se abre un nueva terminal

` python -m venv venv `

## Activación windows
### windows
` .\venv\Scripts\activate  `

si aparece error este comando 

` Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force ` 

luego

` .\venv\Scripts\activate  `

### linux
` source .venv/bin/activate `

## Ejecución
` pytest -v `