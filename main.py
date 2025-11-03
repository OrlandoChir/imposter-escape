@namespace
class SpriteKind:
    Dialogue = SpriteKind.create()

def on_on_created(sprite):
    sprite.follow(player_1, 30)
sprites.on_created(SpriteKind.enemy, on_on_created)

def on_up_pressed():
    global y_direction, x_direction
    y_direction = -200
    x_direction = 0
    animation.run_image_animation(player_1,
        assets.animation("""
            walk_up_animation
            """),
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def initialize_menu():
    pass

def on_overlap_tile(sprite2, location):
    tileUtil.load_connected_map(MapConnectionKind.door1)
    tiles.place_on_random_tile(player_1, tileUtil.door0)
    if tileUtil.current_tilemap() == map_zone_2:
        info.start_countdown(300)
        player_1.x = 26
    else:
        player_1.x = 231
scene.on_overlap_tile(SpriteKind.player, tileUtil.door0, on_overlap_tile)

def on_a_pressed():
    global bullet
    bullet = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . 4 4 . . . . . . .
            . . . . . . 4 5 5 4 . . . . . .
            . . . . . . 2 5 5 2 . . . . . .
            . . . . . . . 2 2 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        player_1,
        x_direction,
        y_direction)
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_down_1
        """))
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    global y_direction, x_direction
    y_direction = 0
    x_direction = -200
    animation.run_image_animation(player_1,
        assets.animation("""
            WalkLeft
            """),
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap(sprite3, otherSprite):
    sprites.destroy(sprite3, effects.spray, 500)
    sprites.destroy(bullet, effects.none, 0)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_right_1
        """))
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_left_1
        """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_countdown_end():
    game.game_over(True)
    game.set_game_over_effect(True, effects.slash)
    game.set_game_over_message(True, "YOU SURVIVED")
    music.stop_all_sounds()
info.on_countdown_end(on_countdown_end)

def on_right_pressed():
    global y_direction, x_direction
    y_direction = 0
    x_direction = 200
    animation.run_image_animation(player_1,
        assets.animation("""
            WalkRight
            """),
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap2(sprite4, otherSprite2):
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_up_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_up_1
        """))
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_map_loaded(tilemap2):
    if tileUtil.current_tilemap() == map_zone_1:
        tileUtil.cover_all_tiles(tileUtil.door0, sprites.dungeon.door_open_east)
    else:
        tileUtil.replace_all_tiles(tileUtil.door0, sprites.builtin.forest_tiles10)
tileUtil.on_map_loaded(on_map_loaded)

def on_down_pressed():
    global y_direction, x_direction
    y_direction = 200
    x_direction = 0
    animation.run_image_animation(player_1,
        assets.animation("""
            walk_down_animation
            """),
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    music.stop_all_sounds()
    game.game_over(False)
    music.play(music.string_playable("G F G A - F E D ", 120),
        music.PlaybackMode.UNTIL_DONE)
    game.set_game_over_message(False, "YOU GOT CAUGHT!")
info.on_life_zero(on_life_zero)

def on_overlap_tile2(sprite5, location2):
    global on_dialogue
    if controller.A.is_pressed():
        if current_zone == "mz_1":
            on_dialogue = True
            
            def on_start_cutscene():
                global on_dialogue
                story.sprite_say_text(player_1, "Already open. . .", 1, 15, story.TextSpeed.SLOW)
                story.sprite_say_text(player_1, "Obviously.", 1, 15, story.TextSpeed.SLOW)
                story.sprite_say_text(player_1,
                    "God forbid I find something useful.",
                    1,
                    15,
                    story.TextSpeed.SLOW)
                story.cancel_all_cutscenes()
                on_dialogue = False
            story.start_cutscene(on_start_cutscene)
            
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile2)

bullet: Sprite = None
x_direction = 0
y_direction = 0
on_dialogue = False
player_1: Sprite = None
current_zone = ""
map_zone_2: tiles.TileMapData = None
map_zone_1: tiles.TileMapData = None
map_zone_1 = tilemap("""
    mz_1
    """)
map_zone_2 = tilemap("""
    mz_2
    """)
current_zone = "mz_1"
tiles.set_current_tilemap(map_zone_1)
player_1 = sprites.create(assets.image("""
    walk_1
    """), SpriteKind.player)
info.set_life(1)
on_dialogue = False
tileUtil.connect_maps(map_zone_1, map_zone_2, MapConnectionKind.door1)
tiles.place_on_random_tile(player_1, sprites.dungeon.collectible_insignia)
player_speed = 200
controller.move_sprite(player_1, 100, 100)

def on_on_update():
    if on_dialogue:
        controller.move_sprite(player_1, 0, 0)
        animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    else:
        controller.move_sprite(player_1, 100, 100)
game.on_update(on_on_update)

def on_update_interval():
    tileUtil.create_sprites_on_tiles(sprites.dungeon.collectible_red_crystal,
        assets.image("""
            Ghost
            """),
        SpriteKind.enemy)
    tileUtil.create_sprites_on_tiles(sprites.dungeon.collectible_blue_crystal,
        assets.image("""
            Ghost
            """),
        SpriteKind.enemy)
game.on_update_interval(5000, on_update_interval)

def on_forever():
    scene.center_camera_at(0, 0)
    scene.camera_follow_sprite(player_1)
    music.play(music.string_playable("C5 A B G A F G E ", 147),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)
