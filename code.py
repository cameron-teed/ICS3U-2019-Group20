#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Dec 2019
# This is the main file for Snakob's forest for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random

import constants


def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # set up the NeoPixels
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    pixels.deinit() # and turn them all off

    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()

        # redraw sprite list

def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 0)
    background.tile(4, 2, 0)
    background.tile(5, 2, 0)
    background.tile(6, 2, 0)
    background.tile(7, 2, 0)  # blank white

   

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("PRESS START")
    text.append(text2)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.0)
        game_splash_scene()

        # redraw sprite list

def game_splash_scene():
    # this function is the game scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


def main_menu_scene():
    # this function is the Main menu

    # an image bank for CircuitPython
    image_bank_3 = stage.Bank.from_bmp16("tree.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    top_right_of_tree = stage.Sprite(image_bank_3 0, 16, 0)
    sprites.append(top_right_of_tree)
    top_middle_of_tree = stage.Sprite(image_bank_3 1, 16, 16)
    sprites.append(top_middle_of_tree)
    top_of_tree = stage.Sprite(image_bank_3 2, 16, 32)
    sprites.append(top_of_tree)
    top_left_of_tree = stage.Sprite(image_bank_3 3, 32, 0)
    sprites.append(top_left_of_tree)
    middle_right_of_tree = stage.Sprite(image_bank_3 4, 32, 16)
    sprites.append(middle_right_of_tree)
    middle_of_tree = stage.Sprite(image_bank_3 5, 32, 32)
    sprites.append(middle_of_tree)
    middle_left_of_tree = stage.Sprite(image_bank_3 6, 48, 0)
    sprites.append(middle_left_of_tree)
    bottem_right_of_tree = stage.Sprite(image_bank_3 7, 48, 16)
    sprites.append(bottem_right_of_tree)
    bottem_midle_of_tree = stage.Sprite(image_bank_3 8, 48, 32)
    sprites.append(bottem_midle_of_tree)
    bottem_left_of_tree = stage.Sprite(image_bank_3 9, 64, 0)
    sprites.append(bottem_left_of_tree)
    verybottem_right_of_tree = stage.Sprite(image_bank_3 10, 64, 16)
    sprites.append(verybottem_right_of_tree)
    verybottem_middle_of_tree = stage.Sprite(image_bank_3 11, 64, 32)
    sprites.append(verybottem_middle_of_tree)
    verybottem_left_of_tree = stage.Sprite(image_bank_3 12, 16, 0)
    sprites.append(verybottem_left_of_tree)
    final_of_tree = stage.Sprite(image_bank_3 13, 16, 0)
    sprites.append(final_of_tree)
 

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()


    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


def game_scene():
    # this function is the game scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


def game_over_scene(final_score):
    # this function is the game over scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


if __name__ == "__main__":
    blank_white_reset_scene()
