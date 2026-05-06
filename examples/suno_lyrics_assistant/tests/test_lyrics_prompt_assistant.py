from examples.suno_lyrics_assistant.lyrics_prompt_assistant import (
    SongRequest,
    generate_template,
)


def test_generate_template_contains_required_sections() -> None:
    req = SongRequest(
        topic="青春與告別",
        mood="明亮中帶感傷",
        genre="mandopop rock",
        voice="male tenor",
        tempo_bpm=110,
    )

    result = generate_template(req)

    assert "system_prompt" in result
    assert "user_prompt" in result
    assert "suno_prompt" in result
    assert "主歌1/副歌" in result["user_prompt"]
    assert "110 BPM" in result["user_prompt"]
    assert "dynamic bridge lift" in result["suno_prompt"]
