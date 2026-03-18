## Decisiones Semanticas

* **`<!DOCTYPE html>` e `<html lang="es">`**: Definen el estandar HTML5 y el idioma español para una correcta interpretacion del navegador.
* **`<meta charset="UTF-8">` y `<meta viewport>`**: Garantizan la visualizacion de caracteres especiales y la adaptacion del diseño a pantallas de celulares.
* **`<header>`**: Agrupa el nombre y la frase representativa como el bloque de identidad inicial.
* **`<main>`**: Identifica el contenido central y unico de la pagina, separandolo de la cabecera y el pie de pagina.
* **`<section>`**: Organiza la informacion en bloques logicos: una para la biografia y otra para los pasatiempos.
* **`<ul>` y `<li>`**: Estructuran los pasatiempos como una lista de elementos relacionados sin un orden de importancia.
* **`<strong>` y `<em>`**: Aportan enfasis y relevancia semantica a palabras clave y frases, permitiendo que los lectores de pantalla las resalten.
* **`<footer>` y `<address>`**: Definen el cierre del documento y marcan especificamente el correo electronico como informacion de contacto.
* **`<time>`**: Permite que las maquinas y navegadores identifiquen una fecha especifica de forma precisa.

## Arbol DOM (Estructura Visual)

```text
Document (html)
---Head (Metadatos y Configuracion)
---Body (Contenido Visible)
       |── Header (Identidad: h1 + p con em)
       |── Main (Contenido Principal)
           |── Section (Yo Soy: h3 + p)
           |── Section (Pasatiempos: h3 + ul con li y strong)
       |── Footer (Contacto y Fecha: address + p con time)
