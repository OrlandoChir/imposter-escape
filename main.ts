namespace SpriteKind {
    export const Dialogue = SpriteKind.create()
}

sprites.onCreated(SpriteKind.Enemy, function on_on_created(sprite: Sprite) {
    sprite.follow(player_1, 30)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    y_direction = -200
    x_direction = 0
    animation.runImageAnimation(player_1, assets.animation`
            walk_up_animation
            `, 200, true)
})
function initialize_menu() {
    
}

scene.onOverlapTile(SpriteKind.Player, tileUtil.door0, function on_overlap_tile(sprite2: Sprite, location: tiles.Location) {
    tileUtil.loadConnectedMap(MapConnectionKind.Door1)
    tiles.placeOnRandomTile(player_1, tileUtil.door0)
    if (tileUtil.currentTilemap() == map_zone_2) {
        info.startCountdown(300)
        player_1.x = 26
    } else {
        player_1.x = 231
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    bullet = sprites.createProjectileFromSprite(img`
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
            `, player_1, x_direction, y_direction)
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
})
controller.down.onEvent(ControllerButtonEvent.Released, function on_down_released() {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`
        walk_down_1
        `)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    
    y_direction = 0
    x_direction = -200
    animation.runImageAnimation(player_1, assets.animation`
            WalkLeft
            `, 200, true)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function on_on_overlap(sprite3: Sprite, otherSprite: Sprite) {
    sprites.destroy(sprite3, effects.spray, 500)
    sprites.destroy(bullet, effects.none, 0)
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.UntilDone)
})
controller.right.onEvent(ControllerButtonEvent.Released, function on_right_released() {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`
        walk_right_1
        `)
})
controller.left.onEvent(ControllerButtonEvent.Released, function on_left_released() {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`
        walk_left_1
        `)
})
info.onCountdownEnd(function on_countdown_end() {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.slash)
    game.setGameOverMessage(true, "YOU SURVIVED")
    music.stopAllSounds()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    
    y_direction = 0
    x_direction = 200
    animation.runImageAnimation(player_1, assets.animation`
            WalkRight
            `, 200, true)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function on_on_overlap2(sprite4: Sprite, otherSprite2: Sprite) {
    info.changeLifeBy(-1)
})
controller.up.onEvent(ControllerButtonEvent.Released, function on_up_released() {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`
        walk_up_1
        `)
})
tileUtil.onMapLoaded(function on_map_loaded(tilemap2: tiles.TileMapData) {
    if (tileUtil.currentTilemap() == map_zone_1) {
        tileUtil.coverAllTiles(tileUtil.door0, sprites.dungeon.doorOpenEast)
    } else {
        tileUtil.replaceAllTiles(tileUtil.door0, sprites.builtin.forestTiles10)
    }
    
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    y_direction = 200
    x_direction = 0
    animation.runImageAnimation(player_1, assets.animation`
            walk_down_animation
            `, 200, true)
})
info.onLifeZero(function on_life_zero() {
    music.stopAllSounds()
    game.gameOver(false)
    music.play(music.stringPlayable("G F G A - F E D ", 120), music.PlaybackMode.UntilDone)
    game.setGameOverMessage(false, "YOU GOT CAUGHT!")
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestOpen, function on_overlap_tile2(sprite5: Sprite, location2: tiles.Location) {
    
    if (controller.A.isPressed()) {
        if (current_zone == "mz_1") {
            on_dialogue = true
            story.startCutscene(function on_start_cutscene() {
                
                story.spriteSayText(player_1, "Already open. . .", 1, 15, story.TextSpeed.Slow)
                story.spriteSayText(player_1, "Obviously.", 1, 15, story.TextSpeed.Slow)
                story.spriteSayText(player_1, "God forbid I find something useful.", 1, 15, story.TextSpeed.Slow)
                story.cancelAllCutscenes()
                on_dialogue = false
            })
        }
        
    }
    
})
let bullet : Sprite = null
let x_direction = 0
let y_direction = 0
let on_dialogue = false
let player_1 : Sprite = null
let current_zone = ""
let map_zone_2 : tiles.TileMapData = null
let map_zone_1 : tiles.TileMapData = null
map_zone_1 = tilemap`
    mz_1
    `
map_zone_2 = tilemap`
    mz_2
    `
current_zone = "mz_1"
tiles.setCurrentTilemap(map_zone_1)
player_1 = sprites.create(assets.image`
    walk_1
    `, SpriteKind.Player)
info.setLife(1)
on_dialogue = false
tileUtil.connectMaps(map_zone_1, map_zone_2, MapConnectionKind.Door1)
tiles.placeOnRandomTile(player_1, sprites.dungeon.collectibleInsignia)
let player_speed = 200
controller.moveSprite(player_1, 100, 100)
game.onUpdate(function on_on_update() {
    if (on_dialogue) {
        controller.moveSprite(player_1, 0, 0)
        animation.stopAnimation(animation.AnimationTypes.All, player_1)
    } else {
        controller.moveSprite(player_1, 100, 100)
    }
    
})
game.onUpdateInterval(5000, function on_update_interval() {
    tileUtil.createSpritesOnTiles(sprites.dungeon.collectibleRedCrystal, assets.image`
            Ghost
            `, SpriteKind.Enemy)
    tileUtil.createSpritesOnTiles(sprites.dungeon.collectibleBlueCrystal, assets.image`
            Ghost
            `, SpriteKind.Enemy)
})
forever(function on_forever() {
    scene.centerCameraAt(0, 0)
    scene.cameraFollowSprite(player_1)
    music.play(music.stringPlayable("C5 A B G A F G E ", 147), music.PlaybackMode.UntilDone)
})
