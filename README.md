<!DOCTYPE html>
<html>
<head>
    <title>App de Recomendación de Películas</title>
</head>
<body>

    <h2>Recomendador de Películas 🎬</h2>

    <label>Escribe tu género favorito:</label>
    <input type="text" id="generoInput">
    <button onclick="recomendar()">Recomendar</button>

    <h3>Recomendaciones:</h3>
    <ul id="resultado"></ul>

    <script>
        const generos = ["Ciencia Ficcion", "Animacion", "Drama", "Accion", "Comedia"];
        const peliculas = [];

        // Generar 10 000 películas automáticamente
        for (let i = 1; i <= 10000; i++) {
            let generoAleatorio = generos[Math.floor(Math.random() * generos.length)];
            peliculas.push({
                titulo: "Pelicula " + i,
                genero: generoAleatorio
            });
        }

        function recomendar() {
            const generoUsuario = document.getElementById("generoInput").value;
            const lista = document.getElementById("resultado");
            lista.innerHTML = "";

            const recomendaciones = peliculas.filter(p =>
                p.genero.toLowerCase() === generoUsuario.toLowerCase()
            );

            if (recomendaciones.length > 0) {
                recomendaciones.slice(0, 20).forEach(p => { // solo muestra 20 para que no se trabe
                    const li = document.createElement("li");
                    li.textContent = p.titulo;
                    lista.appendChild(li);
                });
            } else {
                lista.innerHTML = "<li>No se encontraron recomendaciones</li>";
            }
        }
    </script>

</body>
</html>
