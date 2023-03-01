from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the the Pokemon app!" #welcome to the pokemon app

@app.route('/pokemon-form.html', methods=['GET', 'POST'])
def pokemon():
    pokemon_names = ["bulbasaur", "charmander", "squirtle", "pikachu", "eevee"]

    if request.method == 'POST':
        pokemon_names = request.form['pokemon_names']
        response = request.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        pokemon_data = response.json()

        pokemon_names = pokemon_data['name']
        pokemon_json = response.json()
        abilities = [ability['ability']['name'] for ability in pokemon_json['abilities']]
        sprite_url = pokemon_json['sprites']['front_shiny']
        base_experience = pokemon_json['base_experience']
        attack_base_stat = pokemon_json['stats'][1]['base_stat']
        hp_base_stat = pokemon_json['stats'][0]['base_stat']
        defense_base_stat = pokemon_json['stats'][2]['base_stat']
   


        return render_template('pokemon.html', name = pokemon_names, abilities = abilities,
            sprite_url = sprite_url,
            base_experience = base_experience,
            attack_base_stat =attack_base_stat,
            hp_base_stat = hp_base_stat,
            defense_base_stat=defense_base_stat 
            )
        
    return render_template('pokemon-form.html')


