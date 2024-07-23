#Christian Lazo
testData = [
  {"pregunta": "¿Cómo te dicen tus amigos?", "respuesta":""},
  {"pregunta": "¿Anime, caricatura o serie favorita?", "respuesta":""},
  {"pregunta": "¿Bebida favorita para quitarte el calor?","respuesta":""},
  {"pregunta": "¿Pelicula favorita?", "respuesta":""},
  {"pregunta": "¿Color favorito?", "respuesta":""},
]

print("\nPreguntas******************\n")
for pregunta in testData:
  respuesta = input(pregunta["pregunta"] + " => ")
  pregunta["respuesta"] = respuesta

print("\nRespuestas*****************\n")
for pregunta in testData:
  print(pregunta["pregunta"], " => ", pregunta["respuesta"])