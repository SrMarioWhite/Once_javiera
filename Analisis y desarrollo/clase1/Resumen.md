# 📐 Análisis y desarrollo — Resumen

---

## ¿Por qué importan el análisis y el diseño?

- **El 66% de los proyectos de software fracasan** por requerimientos mal definidos, no por problemas de programación.
- **Análisis** = entender el problema (¿QUÉ se construye?)
- **Diseño** = planear la solución (¿CÓMO se construye?)
- **Regla del 1-10-100:** arreglar un error cuesta $1 en análisis, $10 en diseño, $100 en programación y $1000+ en producción.

---

## Ciclo de Vida del Software

Las 6 fases que todo sistema recorre:

1. **Análisis de Requerimientos** → Especificación de lo que el sistema debe hacer
2. **Diseño** → Arquitectura, diagramas, prototipos
3. **Implementación** → Escritura del código
4. **Pruebas** → Verificación y corrección de errores
5. **Despliegue** → Entrega al usuario final
6. **Mantenimiento** → Correcciones y mejoras continuas

En la práctica el ciclo se **repite** (no es lineal).

---

## Metodologías Estructuradas (Tradicionales)

Filosofía: **planificar todo desde el inicio**.

| Modelo | Característica clave |
|--------|----------------------|
| **Cascada** | Cada fase termina antes de iniciar la siguiente |
| **Modelo en V** | Cada fase de desarrollo tiene su fase de pruebas correspondiente |
| **Espiral** | Iteraciones con análisis de riesgos en cada vuelta |

**Cuándo usarlas:** sistemas críticos (aviación, banca, salud), requerimientos fijos, proyectos regulados.

---

## Metodologías Ágiles

Filosofía: **adaptarse al cambio, entregar valor rápido**.

Nacen en 2001 con el **Manifiesto Ágil**, que valora:
- Individuos e interacciones > procesos y herramientas
- Software funcionando > documentación extensa
- Colaboración con el cliente > negociación de contratos
- Responder al cambio > seguir un plan

| Marco | Característica clave |
|-------|----------------------|
| **Scrum** | Sprints de 1-4 semanas, roles definidos (Product Owner, Scrum Master, Equipo) |
| **Kanban** | Tablero visual con columnas; limita el trabajo en curso |
| **XP** | Programación en pares, TDD, refactorización constante |

**Cuándo usarlas:** startups, apps con requerimientos cambiantes, equipos pequeños (5-9 personas).

---

## Requerimientos

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Funcionales** | Qué hace el sistema | "El sistema permite registrar usuarios" |
| **No funcionales** | Cómo es el sistema | "Responde en menos de 2 segundos" |

**Un buen requerimiento es SMART:** Específico, Medible, Alcanzable, Relevante y con Plazo.

❌ Malo: *"El sistema debe ser seguro."*  
✅ Bueno: *"Las contraseñas se almacenan con bcrypt; el sistema bloquea el acceso tras 5 intentos fallidos."*

Los requerimientos se obtienen mediante entrevistas, encuestas, observación, talleres y prototipos.

---

## Comparativa rápida

| Criterio | Estructuradas | Ágiles |
|----------|--------------|--------|
| Cambios | Difíciles y costosos | Bienvenidos |
| Cliente | Ve el producto al final | Participa constantemente |
| Documentación | Extensa y formal | La mínima necesaria |
| Mejor para | Sistemas críticos y regulados | Productos que evolucionan rápido |

---

*Fuente: [javiera11.vercel.app](https://javiera11.vercel.app/analisis-diseno/uno-curso-analisis-diseno/index.html) · 2026*
