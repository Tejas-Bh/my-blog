Hey there! Welcome to my blog.

Here are a few of my most recent posts:

{% for post in scripts.get_posts()[:5] %}
<blockquote>
    <a href="{{ link_to(post[0]) }}"><b><big>{{ post[1] }}</big></b></a><br />
    <p>{{ post[3] }}<br/>
    <i>Written on {{ post[2] }}</i></p>
    </blockquote></a>
{% endfor %}