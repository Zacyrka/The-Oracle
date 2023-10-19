import discord
from discord.ext import commands
import requests
import read_write_anecdotes
import random
import sqlite_db

TOKEN = 'bot token'
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
anecdotes_file_path = 'D:\Kauno kolegija\Orakulas\Project\Anekdotai'
anecdotes = read_write_anecdotes.read_anecdotes(anecdotes_file_path)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def addPlayer(ctx, vardas, pavarde, pozicija, numeris):
    # Call the 'add_player' function from the 'sqlite_db' module to add a new player to the database.
    sqlite_db.add_player(vardas, pavarde, pozicija, numeris)
    # Send a confirmation message to the Discord channel.
    await ctx.send(f'{vardas} {pavarde} pridėtas į žaidėjų sąrašą.')

@bot.command()
async def playerList(ctx):
    # Retrieve the list of players from the database using the 'get_players' function from the 'sqlite_db' module.
    players = sqlite_db.get_players()
    if players:
        player_list = ''
        for row in players:
            # Construct a player list with their name, position, and jersey number.
            player_list += f'{row[1]} {row[2]}, Pozicija: {row[3]}, Marškinėlių numeris: {row[4]}\n'
        # Create an embedded message with the player list.
        embed = discord.Embed(title="Žaidėjai", description=player_list, color=discord.Color.green())
        # Send the embedded player list message to the Discord channel.
        await ctx.send(embed=embed)
    else:
        # If no players are found in the database, send a message indicating that the player list is empty.
        await ctx.send('Žaidėjų sąrašas tuščias.')

@bot.command()
async def weather(ctx, *, city):
    try:
        # Define the base URL for the OpenWeatherMap API.
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        # Define parameters for the API request, including the city, API key, and units (metric).
        params = {
            'q': city,
            'appid': '8c06fcdbe864bce233313e59058ee6a1',
            'units': 'metric',
        }
        # Send an HTTP GET request to the OpenWeatherMap API with the defined parameters.
        response = requests.get(base_url, params=params)
        # Check if the response status code is 200 (successful response).
        if response.status_code == 200:
            # Parse the JSON response to obtain weather data.
            weather_data = response.json()
            # Send a message to the Discord channel with the weather information.
            await ctx.send(
                f'Weather in {city}: {weather_data["main"]["temp"]}°C, {weather_data["weather"][0]["description"]}')
        else:
            # Send an error message if the API request was unsuccessful.
            await ctx.send(f'Could not retrieve weather data for {city}')
    except Exception as e:
        # Print an error message and send an error message to the Discord channel if any exceptions occur.
        print(f'Error in weather command: {e}')
        await ctx.send('An error occurred while fetching weather data.')

@bot.command()
async def anecdote(ctx):
    # Retrieve a list of anecdotes by calling the read_anecdotes function from the read_write_anecdotes module.
    anecdotes = read_write_anecdotes.read_anecdotes(anecdotes_file_path)
    # Check if there are any anecdotes available.
    if anecdotes:
        # Randomly select an anecdote from the list.
        random_anecdote = random.choice(anecdotes)
        # Send the selected anecdote as a code block in Discord.
        await ctx.send('```' + random_anecdote + '```')
    else:
        # Send a message if there are no anecdotes available.
        await ctx.send('No anecdotes available.')

@bot.command()
async def add(ctx, category: str, *, new_anecdote: str):
    # Check if the provided category is "anecdote."
    if category.lower() == 'anecdote':
        # Call the write_anecdote_to_file function from the read_write_anecdotes module to add the new anecdote to the file.
        read_write_anecdotes.write_anecdote_to_file(anecdotes_file_path, new_anecdote)
        # Append the new anecdote to the list of anecdotes in memory.
        anecdotes.append(new_anecdote)
        # Send a confirmation message that the new anecdote was added.
        await ctx.send(f'Successfully added the new anecdote: "{new_anecdote}"')
    else:
        # Send a message if the provided category is not "anecdote."
        await ctx.send('Invalid category. Use "!add anecdote [your anecdote]" to add a new anecdote.')

bot.run(TOKEN)
