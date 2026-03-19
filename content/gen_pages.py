import os

content = """---
title: Lorem Ipsum
date: 2026-03-18
description: more than just filler text.
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean malesuada, justo quis porttitor imperdiet, augue odio vestibulum nibh, non varius augue mauris eget orci. Sed ullamcorper pulvinar ipsum ac dignissim. Aenean ultricies accumsan condimentum. Mauris id placerat nisi. Proin ultricies nunc tortor, luctus consectetur ipsum eleifend consectetur. Nunc in orci congue, congue neque sed, vulputate libero. Sed bibendum massa ac erat pharetra malesuada sit amet gravida velit. Maecenas dapibus quis ligula in consectetur. Cras viverra risus orci. Integer posuere dui id imperdiet feugiat. Phasellus vestibulum eget elit eu suscipit. Donec vestibulum, metus in ultrices tempor, nibh quam dignissim mauris, at dapibus sem leo nec eros. Aliquam et convallis neque, et tristique felis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

Praesent iaculis semper arcu, vel ultrices turpis auctor vitae. Integer venenatis interdum luctus. Sed vulputate ultrices felis ac rutrum. Nullam a mauris accumsan arcu sollicitudin tempor nec eget sem. Cras placerat tellus nec mauris bibendum porta. Aenean ullamcorper nulla nisl, nec blandit velit laoreet a. Sed malesuada turpis in tempus ultrices. Aenean maximus nunc tortor, a aliquet tortor molestie eget. Morbi non placerat nulla. Aliquam semper augue in tellus dapibus, quis elementum est fermentum. Pellentesque eget felis arcu. Vivamus vitae nibh at odio interdum elementum vitae sed massa. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam elementum velit quis magna egestas, at pretium lectus porta. Morbi vitae justo imperdiet, hendrerit mauris venenatis, tristique purus.
"""

# Create files
for i in range(1, 101):
    filename = f"page{i}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("100 Markdown files created successfully.")