#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from adafruit_servokit import ServoKit

# 16 チャンネル分用意された ServoKit インスタンスを生成
kit = ServoKit(channels=16)

# SG90 サーボ向けにパルス幅レンジをキャリブレーション（必要に応じて調整してください）
# 通常 SG90: 500μs (0°) ～ 2500μs (180°)
kit.servo[0].set_pulse_width_range(500, 2500)  # チャンネル 0 — パン
kit.servo[1].set_pulse_width_range(500, 2500)  # チャンネル 1 — チルト

def pan(angle: float):
    """
    パン動作：チャンネル 0 を指定角度へ移動
    :param angle: 0～180 の範囲
    """
    kit.servo[0].angle = max(0, min(180, angle))

def tilt(angle: float):
    """
    チルト動作：チャンネル 1 を指定角度へ移動
    :param angle: 0～180 の範囲
    """
    kit.servo[1].angle = max(0, min(180, angle))

def demo_sweep():
    """
    パン・チルトを往復させるデモ
    """
    try:
        while True:
            # 0→180° にスイープ
            for a in range(0, 181, 5):
                pan(a)
                tilt(180 - a)
                time.sleep(0.05)
            # 180→0° にスイープ
            for a in range(180, -1, -5):
                pan(a)
                tilt(180 - a)
                time.sleep(0.05)
    except KeyboardInterrupt:
        # Ctrl+C で終了したらサーボをニュートラルへ戻す
        pan(90)
        tilt(90)
        print("\nDemo stopped, servos reset to 90°.")

if __name__ == "__main__":
    # 初期ポジション：両サーボとも 90°（中央）
    pan(90)
    tilt(90)
    time.sleep(1)
    # デモ開始
    demo_sweep()
