# The-Oracle
A Python-based Discord bot for various tasks, including managing a list of players, providing weather information, and sharing anecdotes.
This README provides an overview of the bot's functionality and how to set it up.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Adding Players](#adding-players)
- [Commands](#commands)

## Features

- **Player Management:** The bot can add and display a list of players, including their names, positions, and jersey numbers.

- **Weather Information:** Provides weather data for a given city.

- **Anecdotes:** Shares random anecdotes from a file.

## Requirements

- Python 3.7+
- Discord.py (async)
- SQLite (for managing player data)
- OpenWeatherMap API key (for weather information)
- RapidAPI key (for horoscope - if applicable)

## Adding Players

To add a player to the list, use the !addPlayer command followed by the player's details:
!addPlayer <Name> <LastName> <Position> <Jersey number>

## Commands

!addPlayer vardas pavarde pozicija marskineliu_numeris: Adds a player to the list.
!playerList: Displays the list of players.
!weather city: Provides weather information for a given city.
!anecdote: Shares a random anecdote.
!add anecdote your_anecdote_here: Adds a new anecdote to the list.
