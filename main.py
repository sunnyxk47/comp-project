def on_forever():
    if not (input.button_is_pressed(Button.A)):
        basic.pause(1000)
        music.set_volume(255)
        music.play_tone(988, music.beat(BeatFraction.DOUBLE))
    else:
        music.stop_all_sounds()
basic.forever(on_forever)

def on_forever2():
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    while not (input.button_is_pressed(Button.A)):
        basic.pause(1000)
        basic.show_leds("""
                # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
            """,
            100)
        basic.show_leds("""
                . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
            """,
            100)
        basic.show_leds("""
                # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
            """,
            100)
        basic.show_leds("""
                . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
            """,
            100)
        basic.show_leds("""
                # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
            """,
            100)
        basic.show_leds("""
                . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
            """,
            100)
        basic.show_leds("""
                # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
            """,
            100)
        basic.show_leds("""
                # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
            """,
            100)
        basic.show_leds("""
                . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
            """,
            100)
basic.forever(on_forever2)
