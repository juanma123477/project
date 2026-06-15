from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# Game data stored dynamically in Python dicts
games_data = [
	{
		"id": "fortnite",
		"title": "Fortnite",
		"class": "fortnite",
		"category": "Tips de Construcción y Combate",
		"tips": [
			"<strong>Domina los '90s':</strong> Practica la construcción de torres de 90 grados en el modo creativo para ganar la altura siempre.",
			"<strong>Control de piezas (Piece Control):</strong> Coloca tus propios conos y paredes antes que el enemigo para limitar su movimiento.",
			"<strong>Usa el sonido visual:</strong> Activa los 'Efectos visuales de sonido' en ajustes para ver la dirección exacta de pasos y disparos.",
			"<strong>Gira rápido (Fast Edits):</strong> Practica editar paredes en 0.05 segundos para ganar ventaja en combates cerrados.",
			"<strong>Economía de recursos:</strong> No gastes todos tus materiales en la primera pelea. Prioriza madera en construcciones y piedra en defensas.",
			"<strong>Rotaciones de mapa:</strong> Siempre muévete hacia el círculo 30 segundos antes. Domina los atajos y zonas de loot."
		],
		"fun_things": [
			"<strong>🏗️ Construye un Castillo en el Cielo:</strong> En el modo creativo, construye la estructura más alta y loca posible. ¡Que llegue a las nubes!",
			"<strong>🎯 Desafío de Precisión Pura:</strong> Juega solo con pistola sin construcción. Mata 10 enemigos usando solo headshots.",
			"<strong>🚗 Carreras en Vehículos:</strong> Organiza una carrera amistosa con amigos usando solo vehículos de la isla.",
			"<strong>💣 Bomba de Dinamita:</strong> Completa una partida sin usar armas, solo explosivos. ¡Crea el caos!",
			"<strong>🎭 Modo Pacifista:</strong> Juega una partida sin disparar a nadie. ¿Puedes ganar por posicionamiento puro?",
			"<strong>🌈 Desafío de Colores:</strong> Usa solo skins de un color específico en todas tus partidas durante un día.",
			"<strong>👑 Rey del Terreno:</strong> Consigue todas las skins exclusivas y juega una partida con cada una.",
			"<strong>🎪 Baila en 5 Ubicaciones:</strong> Completa una partida visitando 5 ubicaciones famosas y bailando en cada una.",
			"<strong>🏆 Lluvias de Cajas:</strong> En Squad, intenta conseguir 50 cajas de botín en una sola partida con tu equipo."
		]
	},
	{
		"id": "overwatch",
		"title": "Overwatch 2",
		"class": "overwatch",
		"category": "Tips de Roles y Sinergia",
		"tips": [
			"<strong>Gestión de Ultimates:</strong> No uses todas las habilidades definitivas en una sola pelea. Combina máximo dos por ronda.",
			"<strong>Posicionamiento de Support:</strong> Si juegas soporte, mantente siempre detrás de las esquinas naturales y nunca en campo abierto.",
			"<strong>Agrupación (Grouping up):</strong> Si tu equipo pierde a dos miembros, retrocede. Ir uno a uno sólo alimenta el contador enemigo.",
			"<strong>Contador de Tanques:</strong> Aprende qué heroes counters a los tanques enemigos y ajusta tu pick según su composición.",
			"<strong>Sight Lines:</strong> Posiciónate donde puedas ver a los enemigos sin que ellos te vean. Esto es crucial para iniciaciones ganadas.",
			"<strong>Cooldown Trading:</strong> Si gastas tu habilidad defensiva, mantén distancia hasta que recargue. Conoce los tiempos de cooldown."
		],
		"fun_things": [
			"<strong>⚡ Torneo de 1v1:</strong> Juega solo contra un amigo en el mapa de práctica. ¿Quién gana 5 veces primero?",
			"<strong>🤹 Solo con Melé:</strong> Completa una partida atacando solo con ataques de melee. ¡Nada de habilidades especiales!",
			"<strong>🎪 Rol Roulette:</strong> Que alguien te asigne un rol al azar cada ronda. Domina todos los roles.",
			"<strong>💪 Tanque Rabia:</strong> Juega 10 partidas seguidas como tanque únicamente. Domina el arte de la absorción.",
			"<strong>🏥 Médico Dedicado:</strong> Juega como soporte y termina la partida con máximo número de curaciones registradas.",
			"<strong>🎯 Ultimate Perfecto:</strong> Consigue una partida donde tu equipo gane una pelea importante sin perder a nadie usando un solo Ultimate.",
			"<strong>👥 Sinergia Total:</strong> Juega en equipo y consigue 5 eliminaciones consecutivas sin separarse del grupo.",
			"<strong>🌪️ Todas las Ults:</strong> En una partida, activa TODOS los Ultimates de tu equipo en menos de 30 segundos.",
			"<strong>🏅 Victoria Silenciosa:</strong> Gana una partida sin hablar por voz. Solo pings y comunicación no verbal."
		]
	},
	{
		"id": "cod",
		"title": "Call of Duty",
		"class": "cod",
		"category": "Tips de Movimiento y Aim",
		"tips": [
			"<strong>Cancelación de recarga:</strong> Aprende los tiempos de animación para poder disparar antes si un enemigo te sorprende corriendo.",
			"<strong>Centrado de mira (Centering):</strong> Mantén siempre tu cruz en los puntos donde es más probable que aparezca un rival, no apuntando al suelo.",
			"<strong>Rotación de mapa:</strong> En modos objetivos, empieza a moverte hacia la siguiente zona 20 segundos antes de que expire la actual.",
			"<strong>Control de Recoil:</strong> Aprende el patrón de retroceso de cada arma en el campo de entrenamiento y ajusta tu sensibilidad.",
			"<strong>Angulación de ángulos (Angles):</strong> En defensa, usa ángulos donde el enemigo tiene desventaja de línea de visión. Juega a la esquina.",
			"<strong>Momentum del juego:</strong> Si tu equipo está ganando, presiona. Si estás perdiendo, juega defensivo y busca picks individuales."
		]
	},
	{
		"id": "clashofclans",
		"title": "Clash of Clans",
		"class": "clashofclans",
		"category": "Tips de Estrategia y Defensa",
		"tips": [
			"<strong>Distribución de defensas:</strong> No agrupes todas tus defensas en el centro. Dispersalas para dificultar ataques coordinados.",
			"<strong>Gestión de recursos:</strong> Coloca tus almacenes de oro y elixir en el interior de tu aldea. Protege lo más importante.",
			"<strong>Composición de ejército:</strong> Aprende qué unidades funcionan mejor juntas. Los dragones + curanderas es una combinación poderosa.",
			"<strong>Ataque nocturno:</strong> Practica ataques en la aldea nocturna para recibir recursos adicionales sin riesgo de perder defensas.",
			"<strong>Orden de construcción:</strong> Prioriza torres de fuego e infernales antes que otros edificios de defensa.",
			"<strong>Timing de actualización:</strong> Actualiza defensas mientras construyes construcciones ofensivas. Mantén todo balanceado."
		]
	},
	{
		"id": "clashroyale",
		"title": "Clash Royale",
		"class": "clashroyale",
		"category": "Tips de Estrategia de Cartas",
		"tips": [
			"<strong>Gestión de elixir:</strong> No juegues todas tus cartas a la vez. Espera a que tu elixir se recargue completamente para contraatacar.",
			"<strong>Cartas defensivas:</strong> Mantén siempre una carta defensiva en tu mazo para bloquear ataques de tropas grandes como golem.",
			"<strong>Reconocimiento de decks:</strong> Aprende a identificar el deck del enemigo temprano para ajustar tu estrategia.",
			"<strong>Sobre-defensa:</strong> A veces es mejor dejar pasar un ataque pequeño que gastar mucho elixir en defensa.",
			"<strong>Timing de relajas:</strong> Juega tus cartas en las últimas 30 segundas para tomar decisiones informadas basadas en lo que hace el enemigo.",
			"<strong>Posicionamiento de tropas:</strong> Coloca tus unidades en el carril donde el enemigo no esperaría para obtener el factor sorpresa."
		]
	},
	{
		"id": "brawlstars",
		"title": "Brawl Stars",
		"class": "brawlstars",
		"category": "Tips de Juego Rápido y Posicionamiento",
		"tips": [
			"<strong>Selección de Brawler:</strong> Elige Brawlers que sean efectivos en el mapa de juego actual. Todos tienen fortalezas y debilidades.",
			"<strong>Control de posición:</strong> En modo Asalto de Gemas, mantente cerca de tu equipo para proteger las gemas que recopilas.",
			"<strong>Gestión de Super:</strong> Acumula tu Super en el lugar correcto. Un Super mal cronometrado puede perder el juego.",
			"<strong>Movimiento constante:</strong> No te quedes quieto. Camina de un lado a otro para evitar disparos automáticos del enemigo.",
			"<strong>Aprende los mapas:</strong> Cada mapa tiene puntos clave. Domina donde cubrir para obtener ventaja táctica.",
			"<strong>Elección de Power-ups:</strong> Prioriza Power-ups que te ayuden en tu rol. Soporte? Cura. Daño? Munición."
		]
	},
	{
		"id": "dayz",
		"title": "Day-Z",
		"class": "dayz",
		"category": "Tips de Supervivencia Post-Apocalíptica",
		"tips": [
			"<strong>Búsqueda de agua:</strong> El agua es más importante que la comida. Siempre ten una botella y busca fuentes seguras.",
			"<strong>Evita el ruido:</strong> Los disparos, los pasos y las puertas atraen zombies. Muévete sigilosamente en zonas pobladas.",
			"<strong>Equipo esencial:</strong> Siempre carga una linterna, cuchillo y mochila. Estos items pueden salvarte en una emergencia.",
			"<strong>Encuentros con jugadores:</strong> No confíes en otros jugadores. Ten una salida de emergencia planeada.",
			"<strong>Administración de salud:</strong> Si estás sangrando, aplica un torniquete o vendaje. Sin antibióticos, puedes enfermarte gravemente.",
			"<strong>Exploración inteligente:</strong> Explora en servidor privado primero para aprender patrones de loot y ubicaciones de peligro."
		]
	},
	{
		"id": "godofwar",
		"title": "God of War",
		"class": "godofwar",
		"category": "Tips de Combate y Jefes",
		"tips": [
			"<strong>Domina los combos:</strong> Aprende las combinaciones de botones de tu arma. Los combos largos infligen más daño que golpes individuales.",
			"<strong>Esquiva en el momento correcto:</strong> Esquiva justo cuando el enemigo ataca. Esto activa el ataque de venganza automático.",
			"<strong>Gestión de Rage:</strong> Acumula tu barra de furia atacando. Usa Rage en jefes para infligir daño crítico.",
			"<strong>Bloqueo de ataques especiales:</strong> No todos los ataques pueden bloquearse. Aprende cuales requieren esquivar o parar.",
			"<strong>Mejoras de equipo:</strong> Actualiza tus runas y encantamientos regularmente. Esto hace una gran diferencia en dificultades altas.",
			"<strong>Ataque de relajación:</strong> Después de esquivar, tienes una ventana para atacar. Usa ataques rápidos en este momento."
		]
	},
	{
		"id": "riseofkingdom",
		"title": "Rise of Kingdoms",
		"class": "riseofkingdom",
		"category": "Tips de Estrategia de Imperio",
		"tips": [
			"<strong>Construcción de edificios:</strong> Prioriza granjas y cuarteles al inicio. El crecimiento económico es vital para la expansión.",
			"<strong>Investigación de tecnología:</strong> La tecnología militar es crucial. Investiga armaduras y daño antes de construir ejércitos.",
			"<strong>Gestión de colonias:</strong> Expande a nuevas tierras para obtener recursos pasivos. Las colonias son generadores de oro constantes.",
			"<strong>Alianzas estratégicas:</strong> Únete a una alianza fuerte. Los miembros pueden ayudarte en eventos y defensa conjunta.",
			"<strong>Gestión de generales:</strong> Cada general tiene fortalezas diferentes. Empareja generales según el tipo de batalla.",
			"<strong>Participación en eventos:</strong> Los eventos dan recompensas masivas. Participa en Lost Temple y Ark of Osiris para obtener premios épicos."
		]
	}
]

HTML_HOME = """
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>gamer tips | Guías y Estrategias con Python</title>
	<style>
		:root {
			--bg-principal: #0b0c10;
			--bg-secundario: #1f2833;
			--texto-claro: #c5a059;
			--texto-blanco: #ffffff;
			--neon-azul: #45f3ff;
			--neon-morado: #8a2be2;
		}
		* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
		body { background-color: var(--bg-principal); color: var(--texto-blanco); line-height: 1.6; }
		header {
			background: linear-gradient(90deg, var(--bg-secundario), #0f111a);
			padding: 20px 50px; display: flex; justify-content: space-between; align-items: center;
			border-bottom: 2px solid var(--neon-azul); position: sticky; top: 0; z-index: 1000;
		}
		.logo { cursor: pointer; }
		.logo h1 { font-size: 24px; color: var(--neon-azul); text-transform: uppercase; letter-spacing: 2px; transition: 0.3s; }
		.logo:hover h1 { color: var(--neon-morado); }
		.logo span { color: var(--neon-morado); }
		.fun-btn { display: inline-block; padding: 8px 16px; background: var(--neon-morado); color: var(--texto-blanco); text-decoration: none; border-radius: 5px; font-weight: bold; transition: 0.3s; cursor: pointer; font-size: 14px; }
		.fun-btn:hover { background: var(--neon-azul); }
		nav ul { display: flex; list-style: none; }
		nav ul li { margin-left: 20px; }
		nav ul li a { color: var(--texto-blanco); text-decoration: none; font-weight: bold; transition: 0.3s; cursor: pointer; }
		nav ul li a:hover { color: var(--neon-azul); }
		.hero { text-align: center; padding: 100px 20px; background: radial-gradient(circle, rgba(31,40,51,1) 0%, rgba(11,12,16,1) 100%); }
		.hero h2 { font-size: 45px; margin-bottom: 15px; text-transform: uppercase; }
		.hero p { font-size: 18px; color: #c5a059; max-width: 600px; margin: 0 auto; }
		.contenedor-juegos { max-width: 1200px; margin: 0 auto; padding: 40px 20px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
		.tarjeta-juego { background-color: var(--bg-secundario); border-radius: 10px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); transition: transform 0.3s, box-shadow 0.3s, cursor 0.3s; cursor: pointer; }
		.tarjeta-juego:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(69, 243, 255, 0.2); border-color: var(--neon-azul); }
		.banner-juego { height: 150px; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); }
		.fortnite { background: linear-gradient(135deg, #ff007f, #7f00ff); }
		.overwatch { background: linear-gradient(135deg, #f99e1a, #40b2e6); }
		.cod { background: linear-gradient(135deg, #4a5759, #2b2d42); }
		.clashofclans { background: linear-gradient(135deg, #ff6b35, #f7931e); }
		.clashroyale { background: linear-gradient(135deg, #a6192e, #ffb81c); }
		.brawlstars { background: linear-gradient(135deg, #3669ff, #1a1a2e); }
		.dayz { background: linear-gradient(135deg, #1a1a1a, #404040); }
		.godofwar { background: linear-gradient(135deg, #2a2a2a, #8b0000); }
		.riseofkingdom { background: linear-gradient(135deg, #d4af37, #8b6914); }
		.contenido-tips { padding: 20px; }
		.contenido-tips h3 { margin-bottom: 15px; color: var(--neon-azul); border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 5px; }
		.lista-tips { list-style: none; }
		.lista-tips li { margin-bottom: 12px; position: relative; padding-left: 20px; font-size: 14px; }
		.lista-tips li::before { content: "➔"; position: absolute; left: 0; color: var(--neon-morado); }
		footer { text-align: center; padding: 30px; background-color: #0f111a; border-top: 1px solid rgba(255, 255, 255, 0.1); margin-top: 50px; font-size: 14px; color: #666; }
	</style>
</head>
<body>
	<header>
		<div class="logo" onclick="window.location='/'" style="cursor: pointer;"><h1>gamer<span>tips</span></h1></div>
		<a href="/fun" class="fun-btn">🎮 9 Cosas Divertidas</a>
	</header>

	<section class="hero">
		<h2>Tips para mejorar en tus juegos favoritos</h2>
		<p>Haz click en cualquier juego para ver todos los consejos y estrategias detalladas.</p>
	</section>

	<main class="contenedor-juegos">
		{% for game in games %}
		<article class="tarjeta-juego" onclick="window.location='/game/{{ game.id }}'">
			<div class="banner-juego {{ game.class }}">{{ game.title }}</div>
			<div class="contenido-tips">
				<h3>{{ game.category }}</h3>
				<p style="color: #999; font-size: 13px; margin-top: 10px;">Haz click para ver todos los tips →</p>
			</div>
		</article>
		{% endfor %}
	</main>

	<footer>
		<p>&copy; 2026 gamer tips. Powered by Python & Flask.</p>
	</footer>
</body>
</html>
"""

# HTML template for INDIVIDUAL GAME PAGE
HTML_GAME = """
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>{{ game.title }} - gamer tips</title>
	<style>
		:root {
			--bg-principal: #0b0c10;
			--bg-secundario: #1f2833;
			--texto-claro: #c5a059;
			--texto-blanco: #ffffff;
			--neon-azul: #45f3ff;
			--neon-morado: #8a2be2;
		}
		* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
		body { background-color: var(--bg-principal); color: var(--texto-blanco); line-height: 1.6; }
		header {
			background: linear-gradient(90deg, var(--bg-secundario), #0f111a);
			padding: 20px 50px; display: flex; justify-content: space-between; align-items: center;
			border-bottom: 2px solid var(--neon-azul); position: sticky; top: 0; z-index: 1000;
		}
		.logo { cursor: pointer; }
		.logo h1 { font-size: 24px; color: var(--neon-azul); text-transform: uppercase; letter-spacing: 2px; transition: 0.3s; }
		.logo:hover h1 { color: var(--neon-morado); }
		.logo span { color: var(--neon-morado); }
		.fun-btn { display: inline-block; padding: 8px 16px; background: var(--neon-morado); color: var(--texto-blanco); text-decoration: none; border-radius: 5px; font-weight: bold; transition: 0.3s; cursor: pointer; font-size: 14px; }
		.fun-btn:hover { background: var(--neon-azul); }
		nav ul { display: flex; list-style: none; }
		nav ul li { margin-left: 20px; }
		nav ul li a { color: var(--texto-blanco); text-decoration: none; font-weight: bold; transition: 0.3s; }
		nav ul li a:hover { color: var(--neon-azul); }
		.hero { text-align: center; padding: 60px 20px; background: radial-gradient(circle, rgba(31,40,51,1) 0%, rgba(11,12,16,1) 100%); }
		.hero h2 { font-size: 45px; margin-bottom: 15px; text-transform: uppercase; }
		.back-btn { display: inline-block; margin-top: 20px; padding: 10px 20px; background: var(--neon-azul); color: var(--bg-principal); text-decoration: none; border-radius: 5px; font-weight: bold; transition: 0.3s; }
		.back-btn:hover { background: var(--neon-morado); }
		.contenedor-tips { max-width: 900px; margin: 0 auto; padding: 40px 20px; }
		.tips-grid { display: grid; grid-template-columns: 1fr; gap: 20px; }
		.tip-card { background-color: var(--bg-secundario); border-radius: 10px; padding: 20px; border-left: 4px solid var(--neon-azul); transition: transform 0.3s, box-shadow 0.3s; }
		.tip-card:hover { transform: translateX(10px); box-shadow: 0 5px 15px rgba(69, 243, 255, 0.2); }
		.tip-card strong { color: var(--neon-morado); }
		.banner-game { height: 200px; display: flex; align-items: center; justify-content: center; font-size: 36px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); margin-bottom: 30px; border-radius: 10px; }
		.fortnite { background: linear-gradient(135deg, #ff007f, #7f00ff); }
		.overwatch { background: linear-gradient(135deg, #f99e1a, #40b2e6); }
		.cod { background: linear-gradient(135deg, #4a5759, #2b2d42); }
		.clashofclans { background: linear-gradient(135deg, #ff6b35, #f7931e); }
		.clashroyale { background: linear-gradient(135deg, #a6192e, #ffb81c); }
		.brawlstars { background: linear-gradient(135deg, #3669ff, #1a1a2e); }
		.dayz { background: linear-gradient(135deg, #1a1a1a, #404040); }
		.godofwar { background: linear-gradient(135deg, #2a2a2a, #8b0000); }
		.riseofkingdom { background: linear-gradient(135deg, #d4af37, #8b6914); }
		footer { text-align: center; padding: 30px; background-color: #0f111a; border-top: 1px solid rgba(255, 255, 255, 0.1); margin-top: 50px; font-size: 14px; color: #666; }
	</style>
</head>
<body>
	<header>
		<div class="logo" onclick="window.location='/'" style="cursor: pointer;"><h1>gamer<span>tips</span></h1></div>
		<a href="/fun" class="fun-btn">🎮 9 Cosas Divertidas</a>
	</header>

	<section class="hero">
		<div class="banner-game {{ game.class }}">{{ game.title }}</div>
		<h2>{{ game.category }}</h2>
		<a href="/" class="back-btn">← Volver al inicio</a>
	</section>

	<main class="contenedor-tips">
		<div class="tips-grid">
			{% for tip in game.tips %}
			<div class="tip-card">
				{{ tip | safe }}
			</div>
			{% endfor %}
		</div>
	</main>

	<footer>
		<p>&copy; 2026 gamer tips. Powered by Python & Flask.</p>
	</footer>
</body>
</html>
"""

# HTML template for FUN THINGS PAGE
HTML_FUN = """
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>9 Cosas Divertidas - gamer tips</title>
	<style>
		:root {
			--bg-principal: #0b0c10;
			--bg-secundario: #1f2833;
			--texto-claro: #c5a059;
			--texto-blanco: #ffffff;
			--neon-azul: #45f3ff;
			--neon-morado: #8a2be2;
		}
		* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
		body { background-color: var(--bg-principal); color: var(--texto-blanco); line-height: 1.6; }
		header {
			background: linear-gradient(90deg, var(--bg-secundario), #0f111a);
			padding: 20px 50px; display: flex; justify-content: space-between; align-items: center;
			border-bottom: 2px solid var(--neon-azul); position: sticky; top: 0; z-index: 1000;
		}
		.logo { cursor: pointer; }
		.logo h1 { font-size: 24px; color: var(--neon-azul); text-transform: uppercase; letter-spacing: 2px; transition: 0.3s; }
		.logo:hover h1 { color: var(--neon-morado); }
		.logo span { color: var(--neon-morado); }
		.hero { text-align: center; padding: 80px 20px; background: radial-gradient(circle, rgba(31,40,51,1) 0%, rgba(11,12,16,1) 100%); }
		.hero h2 { font-size: 45px; margin-bottom: 15px; text-transform: uppercase; }
		.hero p { font-size: 18px; color: #c5a059; max-width: 600px; margin: 0 auto; }
		.back-btn { display: inline-block; margin-top: 20px; padding: 10px 20px; background: var(--neon-azul); color: var(--bg-principal); text-decoration: none; border-radius: 5px; font-weight: bold; transition: 0.3s; cursor: pointer; }
		.back-btn:hover { background: var(--neon-morado); }
		.contenedor-cosas { max-width: 1200px; margin: 0 auto; padding: 40px 20px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
		.cosa-card { background-color: var(--bg-secundario); border-radius: 10px; overflow: hidden; border: 2px solid var(--neon-morado); transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s; }
		.cosa-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(138, 43, 226, 0.3); border-color: var(--neon-azul); }
		.cosa-header { background: linear-gradient(135deg, #8a2be2, #45f3ff); padding: 30px 20px; text-align: center; }
		.cosa-numero { font-size: 48px; font-weight: bold; color: #fff; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); }
		.cosa-contenido { padding: 20px; }
		.cosa-contenido h3 { color: var(--neon-azul); margin-bottom: 10px; font-size: 20px; }
		.cosa-contenido p { color: #ddd; font-size: 15px; line-height: 1.8; }
		.cosa-icon { font-size: 40px; margin-bottom: 10px; }
		footer { text-align: center; padding: 30px; background-color: #0f111a; border-top: 1px solid rgba(255, 255, 255, 0.1); margin-top: 50px; font-size: 14px; color: #666; }
	</style>
</head>
<body>
	<header>
		<div class="logo" onclick="window.location='/'" style="cursor: pointer;"><h1>gamer<span>tips</span></h1></div>
	</header>

	<section class="hero">
		<h2>9 Cosas Divertidas en Gaming</h2>
		<p>Desafíos y actividades épicas que puedes hacer en todos tus juegos favoritos</p>
		<a href="/" class="back-btn">← Volver</a>
	</section>

	<main class="contenedor-cosas">
		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">1</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">🏆</div>
				<h3>Desafío Sin Mirar</h3>
				<p>Juega una partida completa sin mirar la pantalla mientras escuchas los sonidos. ¡Depende completamente del audio!</p>
			</div>
		</div>

		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">2</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">⚡</div>
				<h3>Velocidad Extrema</h3>
				<p>Completa una misión o nivel en el menor tiempo posible. Compite contra tu propio récord personal.</p>
			</div>
		</div>

		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">3</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">🎭</div>
				<h3>Rol Play Extremo</h3>
				<p>Elige un personaje y juega SOLO con ese personaje. No cambies nunca, sin importar la situación.</p>
			</div>
		</div>

		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">4</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">🔇</div>
				<h3>Silencio Total</h3>
				<p>Juega sin música ni efectos de sonido. Solo los diálogos. Descubre cuánto te ayuda el audio a jugar.</p>
			</div>
		</div>

		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">5</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">💪</div>
				<h3>Modo Hardcore</h3>
				<p>Juega en la dificultad máxima sin items especiales. Solo habilidades básicas. ¡Que empiece la adrenalina!</p>
			</div>
		</div>

		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">6</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">🌍</div>
				<h3>Explorador Total</h3>
				<p>Descubre cada rincón del mapa. Encuentra todos los secretos, tesoros ocultos y localizaciones especiales.</p>
			</div>
		</div>

		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">7</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">🎯</div>
				<h3>Precisión Perfecta</h3>
				<p>Intenta completar una misión sin cometer un solo error. Cada acción debe ser perfecta y calculada.</p>
			</div>
		</div>

		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">8</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">🤝</div>
				<h3>Juega con Amigos</h3>
				<p>Convierte tu sesión en multijugador cooperativo. Coordina con amigos para lograr objetivos épicos juntos.</p>
			</div>
		</div>

		<div class="cosa-card">
			<div class="cosa-header">
				<div class="cosa-numero">9</div>
			</div>
			<div class="cosa-contenido">
				<div class="cosa-icon">🎬</div>
				<h3>Graba tu Gameplay</h3>
				<p>Documenta tus mejores momentos. Crea montajes épicos, tutoriales o comparte tus logros con la comunidad.</p>
			</div>
		</div>
	</main>

	<footer>
		<p>&copy; 2026 gamer tips. Powered by Python & Flask.</p>
	</footer>
</body>
</html>
"""

@app.route('/')
def home():
	return render_template_string(HTML_HOME, games=games_data)

@app.route('/fun')
def fun_things():
	return render_template_string(HTML_FUN)

@app.route('/game/<game_id>')
def game(game_id):
	game = next((g for g in games_data if g['id'] == game_id), None)
	if game is None:
		return redirect('/')
	return render_template_string(HTML_GAME, game=game, all_games=games_data)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(__import__('os').environ.get('PORT', '5001')))
