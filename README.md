# Kata 30

Version 2.0 de la [kata 29](https://www.codewars.com/kata/525f50e3b73515a6db000b83), se seguirán las mimas reglas que establece [esa actividad](https://www.codewars.com/kata/525f50e3b73515a6db000b83) y además podrás recibir palabras a demás de números utilizando [phone words](https://es.wikipedia.org/wiki/Phonewords)

Ejemplo: [1, 2, 3, L, L, A, M, E, Y, A] => (123) 552-6392

## Usando phones.py en modo CLI

```bash
python phones.py 664 LLAME YA
```

## Corriendo los tests

### Requisitos

- virtualenv (python -m pip install -U virtualenv)

### Instalar el ambiente

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usando pytest

```bash
pytest
```
