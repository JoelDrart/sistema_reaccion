from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Definir la ruta principal
@app.route('/')
def index():
    return render_template('index.html')

base_conocimiento = {
    "inicio": {
        "pregunta": "¿Qué tema sobre videojuegos te interesa explorar?",
        "respuestas": {
            "1": {
                "nombreOpcion": "Géneros de Videojuegos",
                "flujoSiguiente": "generos_videojuegos"
            },
            "2": {
                "nombreOpcion": "Desarrollo de Videojuegos",
                "flujoSiguiente": "desarrollo_videojuegos"
            },
            "3": {
                "nombreOpcion": "Historia de los Videojuegos",
                "flujoSiguiente": "historia_videojuegos"
            },
            "4": {
                "nombreOpcion": "Plataformas",
                "flujoSiguiente": "plataformas_videojuegos"
            },
            "5": {
                "nombreOpcion": "Tendencias Actuales",
                "flujoSiguiente": "tendencias_videojuegos"
            },
            "6": {
                "nombreOpcion": "Comunidades y Cultura Gamer",
                "flujoSiguiente": "comunidades_cultura_gamer"
            }
        }
    },
    "generos_videojuegos": {
        "pregunta": "¿Qué género te interesa?",
        "respuestas": {
            "1": {
                "nombreOpcion": "Acción",
                "flujoSiguiente": "genero_accion"
            },
            "2": {
                "nombreOpcion": "RPG",
                "flujoSiguiente": "genero_rpg"
            },
            "3": {
                "nombreOpcion": "Estrategia",
                "flujoSiguiente": "genero_estrategia"
            },
            "4": {
                "nombreOpcion": "Simulación",
                "flujoSiguiente": "genero_simulacion"
            },
            "5": {
                "nombreOpcion": "Indie",
                "flujoSiguiente": "genero_indie"
            },
            "6": {
                "nombreOpcion": "Otro",
                "flujoSiguiente": "genero_otro"
            }
        }
    },
    "desarrollo_videojuegos": {
        "pregunta": "¿Qué aspecto del desarrollo de videojuegos te interesa?",
        "respuestas": {
            "1": {
                "nombreOpcion": "Motores Gráficos",
                "flujoSiguiente": "motores_graficos"
            },
            "2": {
                "nombreOpcion": "Programación",
                "flujoSiguiente": "programacion_videojuegos"
            },
            "3": {
                "nombreOpcion": "Diseño Narrativo",
                "flujoSiguiente": "diseno_narrativo"
            },
            "4": {
                "nombreOpcion": "Modelado 3D",
                "flujoSiguiente": "modelado_3d"
            },
            "5": {
                "nombreOpcion": "Audio y Música",
                "flujoSiguiente": "audio_musica"
            }
        }
    },
    "historia_videojuegos": {
        "pregunta": "¿Qué época histórica te interesa explorar?",
        "respuestas": {
            "1": {
                "nombreOpcion": "Los Orígenes",
                "flujoSiguiente": "origenes_videojuegos"
            },
            "2": {
                "nombreOpcion": "Años 80 y 90",
                "flujoSiguiente": "anos_80_90"
            },
            "3": {
                "nombreOpcion": "Siglo XXI",
                "flujoSiguiente": "siglo_21_videojuegos"
            }
        }
    },
    "plataformas_videojuegos": {
        "pregunta": "¿Qué plataforma deseas explorar?",
        "respuestas": {
            "1": {
                "nombreOpcion": "Consolas",
                "flujoSiguiente": "plataformas_consolas"
            },
            "2": {
                "nombreOpcion": "PC",
                "flujoSiguiente": "plataformas_pc"
            },
            "3": {
                "nombreOpcion": "Móviles",
                "flujoSiguiente": "plataformas_moviles"
            },
            "4": {
                "nombreOpcion": "Realidad Virtual",
                "flujoSiguiente": "plataformas_rv"
            }
        }
    },
    "tendencias_videojuegos": {
        "pregunta": "¿Qué tendencia te interesa?",
        "respuestas": {
            "1": {
                "nombreOpcion": "Streaming",
                "flujoSiguiente": "tendencia_streaming"
            },
            "2": {
                "nombreOpcion": "Juegos como Servicio",
                "flujoSiguiente": "tendencia_gas"
            },
            "3": {
                "nombreOpcion": "eSports",
                "flujoSiguiente": "tendencia_esports"
            },
            "4": {
                "nombreOpcion": "Inteligencia Artificial en Videojuegos",
                "flujoSiguiente": "tendencia_ia"
            }
        }
    },
    "comunidades_cultura_gamer": {
        "pregunta": "¿Sobre qué comunidad o aspecto cultural deseas aprender?",
        "respuestas": {
            "1": {
                "nombreOpcion": "Comunidades Online",
                "flujoSiguiente": "comunidades_online"
            },
            "2": {
                "nombreOpcion": "Cultura Gamer",
                "flujoSiguiente": "cultura_gamer"
            },
            "3": {
                "nombreOpcion": "Eventos y Torneos",
                "flujoSiguiente": "eventos_torneos"
            }
        }
    },
    "genero_accion": {
        "respuesta_final": "Los juegos de acción suelen centrarse en combates rápidos, reflejos y desafíos intensos. Ejemplos incluyen 'Call of Duty' y 'Fortnite'."
    },
    "genero_rpg": {
        "respuesta_final": "Los RPGs (Juegos de Rol) permiten a los jugadores desarrollar personajes y seguir historias profundas. Ejemplos: 'The Witcher', 'Final Fantasy'."
    },
    "genero_estrategia": {
        "respuesta_final": "Los juegos de estrategia requieren planificación y tácticas, como 'Age of Empires' o 'StarCraft'."
    },
    "genero_simulacion": {
        "respuesta_final": "Los juegos de simulación recrean escenarios reales o ficticios, como 'The Sims' o 'Flight Simulator'."
    },
    "genero_indie": {
        "respuesta_final": "Los juegos indie son desarrollados por estudios pequeños o individuales. Ejemplo: 'Hollow Knight', 'Stardew Valley'."
    },
    "genero_otro": {
        "respuesta_final": "Existen muchos géneros como terror, aventura gráfica y música. Ejemplo: 'Amnesia', 'Monkey Island'."
    },
    "motores_graficos": {
        "respuesta_final": "Motores populares incluyen Unity, Unreal Engine y Godot, que son herramientas clave para crear videojuegos."
    },
    "programacion_videojuegos": {
        "respuesta_final": "El desarrollo de videojuegos usa lenguajes como C++, C#, y Python, dependiendo del motor gráfico."
    },
    "diseno_narrativo": {
        "respuesta_final": "El diseño narrativo crea historias inmersivas y emocionantes, uniendo narrativa y gameplay."
    },
    "modelado_3d": {
        "respuesta_final": "El modelado 3D utiliza software como Blender o Maya para crear personajes y entornos realistas."
    },
    "audio_musica": {
        "respuesta_final": "El diseño de audio es esencial, con herramientas como FMOD y Wwise para integrar música y efectos."
    },
    "origenes_videojuegos": {
        "respuesta_final": "Los videojuegos nacieron en los 70 con clásicos como 'Pong' y 'Space Invaders'."
    },
    "anos_80_90": {
        "respuesta_final": "Esta época vio el auge de consolas como NES y PlayStation, con juegos icónicos como 'Super Mario Bros.'"
    },
    "siglo_21_videojuegos": {
        "respuesta_final": "El siglo XXI trajo gráficos avanzados, realismo y experiencias online masivas como 'World of Warcraft'."
    },
    "plataformas_consolas": {
        "respuesta_final": "Consolas como PlayStation, Xbox y Nintendo Switch lideran el mercado con exclusivos destacados."
    },
    "plataformas_pc": {
        "respuesta_final": "El PC ofrece versatilidad, con gráficos avanzados y una amplia biblioteca de juegos."
    },
    "plataformas_moviles": {
        "respuesta_final": "Los juegos móviles como 'Clash of Clans' o 'Genshin Impact' son populares por su accesibilidad."
    },
    "plataformas_rv": {
        "respuesta_final": "La realidad virtual ofrece experiencias inmersivas con dispositivos como Oculus Quest y PlayStation VR."
    },
    "tendencia_streaming": {
        "respuesta_final": "Plataformas como Twitch y YouTube Gaming dominan el streaming de videojuegos."
    },
    "tendencia_gas": {
        "respuesta_final": "Juegos como servicio (GaaS) incluyen actualizaciones regulares, como 'Fortnite' o 'Apex Legends'."
    },
    "tendencia_esports": {
        "respuesta_final": "Los eSports reúnen jugadores profesionales en competiciones globales, con títulos como 'League of Legends'."
    },
    "tendencia_ia": {
        "respuesta_final": "La inteligencia artificial mejora comportamientos de NPC y genera mundos dinámicos en juegos como 'No Man's Sky'."
    },
    "comunidades_online": {
        "respuesta_final": "Comunidades online conectan jugadores globalmente, creando espacios para compartir estrategias y experiencias."
    },
    "cultura_gamer": {
        "respuesta_final": "La cultura gamer abarca memes, mods, y un lenguaje propio que evoluciona con los años."
    },
    "eventos_torneos": {
        "respuesta_final": "Eventos como E3 y torneos de eSports son fundamentales para la comunidad gamer."
    }
};


@app.route('/pregunta/<id>')
def obtener_pregunta(id):
    # Busca la pregunta en la base de conocimiento
    pregunta = base_conocimiento.get(id, {})
    if "respuesta_final" in pregunta:
        # Si es una respuesta final, devuelve un mensaje
        return jsonify({
            "pregunta": "Respuesta final:",
            "respuestas": None,
            "respuesta_final": pregunta["respuesta_final"]
        })
    return jsonify({
        "pregunta": pregunta.get("pregunta", "No se encontró la pregunta."),
        "respuestas": pregunta.get("respuestas", {})
    })


if __name__ == '__main__':
    app.run(debug=True)
