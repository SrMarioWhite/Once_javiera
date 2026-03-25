# Explicacion Del Formulario.

## Configuración General del Formulario
El contenedor principal utiliza la etiqueta **form** con la clase **formulario-contacto**. Esta etiqueta incluye el atributo **action** configurado actualmente con un símbolo de almohadilla y el atributo **method** establecido como **post** para el envío seguro de la información al servidor. La presencia del atributo **novalidate** es fundamental ya que indica al navegador que no debe aplicar sus validaciones automáticas por defecto lo que suele hacerse cuando se pretende gestionar la validación mediante scripts personalizados de JavaScript.

## Estructura de Datos Personales
El código organiza el nombre y el correo electrónico dentro de un contenedor **div** llamado **fila-doble** para facilitar un diseño de columnas. Cada entrada de datos está envuelta en un **div** de clase **campo** para mantener la coherencia visual. La etiqueta **label** se vincula a cada entrada mediante el atributo **for** que coincide con el **id** del campo correspondiente. El campo de nombre es un **input type="text"** que exige un mínimo de dos caracteres y un máximo de sesenta mientras que el campo de correo es un **input type="email"** que valida automáticamente la estructura de la dirección electrónica y utiliza el atributo **autocomplete** para mejorar la rapidez del llenado.

## Selección Categorizada de Consultas
Para elegir el motivo del contacto se utiliza el elemento **select** el cual contiene etiquetas **optgroup**. Estas etiquetas sirven para clasificar las opciones en categorías lógicas como Soporte Información u Otros facilitando la navegación del usuario dentro del menú desplegable. Cada opción individual dentro de estos grupos posee un atributo **value** que representa el dato técnico que recibirá el sistema al procesar el formulario.

## Campos de Asunto y Edad
El formulario dispone de un campo de texto simple para el asunto con un límite de cien caracteres. Inmediatamente después se encuentra un campo de tipo **number** destinado a la edad que restringe la entrada a valores entre quince y noventa y nueve. Un detalle importante a corregir en tu código es que el campo de edad actualmente utiliza el mismo **id** y **name** que el campo de asunto lo que provocaría que los datos se sobrescriban o causen errores al enviarse. Cada campo debe tener identificadores y nombres únicos.

## Mensajes de Texto Extenso
Para la descripción de la consulta se emplea un elemento **textarea**. A diferencia de los campos de texto normales este permite múltiples líneas y su tamaño se define inicialmente con el atributo **rows**. Posee validaciones de longitud mínima de veinte caracteres y máxima de mil para asegurar que el mensaje sea descriptivo pero conciso.

## Canales de Comunicación y Teléfono
La sección de preferencia de contacto utiliza botones de radio **input type="radio"**. Al compartir el mismo nombre de atributo **name** el navegador garantiza que solo se pueda elegir una opción entre email WhatsApp o llamada. El campo de teléfono es un **input type="tel"** que incorpora un atributo **pattern** con una expresión regular permitiendo validar que el formato ingresado sea coherente con un número telefónico internacional o local.

## Consentimientos Legales y Botones de Acción
La parte final del formulario incluye dos casillas de verificación **input type="checkbox"**. La primera es obligatoria para aceptar los términos y la política de privacidad mientras que la segunda es opcional para la suscripción a novedades. El cierre del formulario lo componen dos elementos **button**. El botón de tipo **submit** es el encargado de enviar los datos recolectados y el botón de tipo **reset** permite al usuario borrar toda la información introducida con un solo clic.

---