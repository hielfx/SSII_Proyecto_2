# Proyecto 2 de la Asignatura Seguridad en Sistemas Informáticos e Internet
####PSI 2. INTRANS. VERIFICADORES DE INTEGRIDAD EN LA TRANSMISIÓN PUNTO-PUNTO DE LA INFORMACIÓN

Desarrollo de un verificador de integridad a través de sockets que cumple con los siguientes objetivos de seguridad:

1. **FR01** – Integridad de los mensajes: El servidor deberá comprobar la integridad de los mensajes en cada recepción.
2. **FR02** – Envío de NONCEs: El servidor deberá comprobar los NONCE enviados por el cliente para así evitar posibles ataques de replay.
3. **FR03** – Frecuencia de reporte: El sistema deberá reportar mensualmente las tendencias del estado de cumplimiento de las políticas de integridad.
4. **FR04** – Formato de reporte: El sistema deberá realizar el reporte como un gráfico de línea que represente el ratio de integridad diaria de los mensajes.
5. **FR05** – Colisiones: El sistema deberá evitar colisiones al utilizar los hashing seguros. • FR06 – Multi SO: El sistema deberá poder ejecutarse en diferentes sistemas operativos.
6. **IR01** – Logs: El servidor deberá almacenar un fichero con los logs de lo que ocurre en el sistema desde que se ejecuta el servidor hasta que se detiene y cierra.
7. **IR02** – Información del mensaje: Se deberá almacenar información acerca del mensaje enviado,
en concreto: NONCE, fecha de inserción, HMAC, conservación de la integridad
