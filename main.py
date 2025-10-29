@namespace
class SpriteKind:
    Dialogue = SpriteKind.create()

def on_up_pressed():
    animation.run_image_animation(player_1,
        assets.animation("""
            walk_up_animation
            """),
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    tileUtil.load_connected_map(MapConnectionKind.door1)
    tiles.place_on_random_tile(player_1, tileUtil.door0)
    if tileUtil.current_tilemap() == map_zone_2:
        player_1.x = 26
    else:
        player_1.x = 231
scene.on_overlap_tile(SpriteKind.player, tileUtil.door0, on_overlap_tile)

def on_down_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_down_1
        """))
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    animation.run_image_animation(player_1,
        assets.animation("""
            WalkLeft
            """),
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

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

def on_right_pressed():
    animation.run_image_animation(player_1,
        assets.animation("""
            WalkRight
            """),
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_up_released():
    animation.stop_animation(animation.AnimationTypes.ALL, player_1)
    player_1.set_image(assets.image("""
        walk_up_1
        """))
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    animation.run_image_animation(player_1,
        assets.animation("""
            walk_down_animation
            """),
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_overlap_tile2(sprite2, location2):
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

on_dialogue = False
player_1: Sprite = None
current_zone = ""
map_zone_2: tiles.TileMapData = None
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

def on_forever():
    scene.center_camera_at(0, 0)
    scene.camera_follow_sprite(player_1)
    music.play(music.string_playable("C5 A B G A F G E ", 115),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)
