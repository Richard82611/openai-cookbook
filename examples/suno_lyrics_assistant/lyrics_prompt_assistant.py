"""CLI tool to generate Chinese lyric drafts and Suno-style prompt guidance.

This utility does not call Suno directly. It creates structured prompts users can
paste into their own music generation workflow.
"""

from __future__ import annotations

from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class SongRequest:
    topic: str
    mood: str
    genre: str
    voice: str
    tempo_bpm: int
    era_style: str = "modern mandopop"


class LyricsPromptAssistant:
    """Builds high-quality Chinese lyric and composition prompts."""

    def build_system_prompt(self) -> str:
        return dedent(
            """
            你是華語頂尖作詞顧問與編曲提示詞設計師。
            你的任務是：
            1) 先給出可直接用於創作的中文歌詞草稿（主歌/副歌/橋段）。
            2) 再給出可用於 Suno 類型音樂生成器的精準提示詞。
            3) 歌詞需避免陳腔濫調，保留畫面感、節奏感、可唱性。
            4) 回覆需包含：歌名、風格描述、關鍵意象、歌詞、提示詞、負面提示詞。
            """
        ).strip()

    def build_user_prompt(self, req: SongRequest) -> str:
        return dedent(
            f"""
            請幫我產出一首中文歌，需求如下：
            - 主題：{req.topic}
            - 情緒：{req.mood}
            - 曲風：{req.genre}
            - 演唱聲線：{req.voice}
            - 速度：{req.tempo_bpm} BPM
            - 時代質感：{req.era_style}

            請輸出：
            A. 一句吸引人的歌名（繁體中文）
            B. 風格與編曲摘要（80字內）
            C. 歌詞（主歌1/副歌/主歌2/副歌/橋段/尾副歌）
            D. Suno 提示詞（包含：風格、樂器、節奏、聲線、情緒轉折、混音關鍵字）
            E. 負面提示詞（避免俗套詞、避免過度重複、避免咬字不清）
            """
        ).strip()

    def build_suno_prompt_block(self, req: SongRequest) -> str:
        return (
            f"Mandopop, {req.genre}, {req.mood}, {req.tempo_bpm} BPM, "
            f"{req.voice} vocal, {req.era_style}, cinematic intro, "
            "memorable hook chorus, dynamic bridge lift, clean vocal mix, "
            "warm bass, wide stereo synth layers, polished mastering"
        )


def generate_template(req: SongRequest) -> dict[str, str]:
    assistant = LyricsPromptAssistant()
    return {
        "system_prompt": assistant.build_system_prompt(),
        "user_prompt": assistant.build_user_prompt(req),
        "suno_prompt": assistant.build_suno_prompt_block(req),
    }


if __name__ == "__main__":
    sample = SongRequest(
        topic="凌晨三點的城市與未寄出的訊息",
        mood="遺憾但克制",
        genre="synth-pop with piano",
        voice="female airy mezzo",
        tempo_bpm=96,
    )
    template = generate_template(sample)
    for key, value in template.items():
        print(f"\n===== {key} =====\n{value}\n")
