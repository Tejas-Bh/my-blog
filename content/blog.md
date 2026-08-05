---
special: blog
title: Blog and Project Notes
description: Howdy, welcome to my blog! Here, you can find technical write-ups, radio logs, music, and any other things I find fascinating.
---

__All of my posts, sorted by date.__

<!-- {% for post in scripts.get_posts()[:5] %}
<blockquote>
    <a href="{{ link_to(post[0]) }}"><b><big>{{ post[1] }}</big></b></a><br />
    <p>{{ post[3] }}<br/>
    <i>Written on {{ post[2] }}</i></p>
    </blockquote></a>
{% endfor %} -->


{% for post in scripts.get_posts() %}
<div class="space-y-6">
    <article class="theme-card border-2 p-6 rounded-xl space-y-3 hover:border-amber-400 transition-colors">
        <div class="flex flex-wrap justify-between items-center gap-2 text-xs font-mono theme-subtext">
            <span class="theme-amber font-bold">{{ post[2] }}</span>
        </div>
        <h3 class="text-xl font-bold theme-heading hover:theme-cyan">
            <a href="{{ link_to(post[0]) }}" class="focus:outline-none focus:underline theme-text">{{ post[1] }}</a>
        </h3>
        <p class="text-sm theme-subtext leading-relaxed">
            {{ post[3] }}
        </p>
    </article>
</div>
{% endfor %}