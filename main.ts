namespace SpriteKind {
    export const Dialogue = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    player_1,
    assets.animation`walk_up_animation`,
    200,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, tileUtil.door0, function (sprite, location) {
    tileUtil.loadConnectedMap(MapConnectionKind.Door1)
    tiles.placeOnRandomTile(player_1, tileUtil.door0)
    if (tileUtil.currentTilemap() == map_zone_2) {
        player_1.x = 26
    } else {
        player_1.x = 231
    }
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`walk_down_1`)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    player_1,
    assets.animation`WalkLeft`,
    200,
    true
    )
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`walk_right_1`)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`walk_left_1`)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    player_1,
    assets.animation`WalkRight`,
    200,
    true
    )
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, player_1)
    player_1.setImage(assets.image`walk_up_1`)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    player_1,
    assets.animation`walk_down_animation`,
    200,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestOpen, function (sprite, location) {
    if (controller.A.isPressed()) {
        if (current_zone == "mz_1") {
            on_dialogue = true
            story.startCutscene(function () {
                story.spriteSayText(player_1, "Already open. . .", 1, 15, story.TextSpeed.Slow)
                story.spriteSayText(player_1, "Obviously.", 1, 15, story.TextSpeed.Slow)
                story.spriteSayText(player_1, "God forbid I find something useful.", 1, 15, story.TextSpeed.Slow)
                story.cancelAllCutscenes()
                on_dialogue = false
            })
        }
    }
})
let on_dialogue = false
let player_1: Sprite = null
let current_zone = ""
let map_zone_2: tiles.TileMapData = null
let map_zone_1 = tilemap`mz_1`
map_zone_2 = tilemap`mz_2`
current_zone = "mz_1"
tiles.setCurrentTilemap(map_zone_1)
player_1 = sprites.create(assets.image`walk_1`, SpriteKind.Player)
on_dialogue = false
tileUtil.connectMaps(map_zone_1, map_zone_2, MapConnectionKind.Door1)
tiles.placeOnRandomTile(player_1, sprites.dungeon.collectibleInsignia)
let player_speed = 200
controller.moveSprite(player_1, 100, 100)
game.onUpdate(function () {
    if (on_dialogue) {
        controller.moveSprite(player_1, 0, 0)
        animation.stopAnimation(animation.AnimationTypes.All, player_1)
    } else {
        controller.moveSprite(player_1, 100, 100)
    }
})
forever(function () {
    scene.centerCameraAt(0, 0)
    scene.cameraFollowSprite(player_1)
    music.play(music.stringPlayable("C5 A B G A F G E ", 147), music.PlaybackMode.UntilDone)
})
