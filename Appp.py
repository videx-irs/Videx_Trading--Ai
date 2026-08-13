from flask import Flask, jsonify, request

App = Flask(__name__)

# Temporary in-memory posts
posts = [
    {
        "id": 1,
        "username": "VIDEX",
        "text": "Welcome to VIDEX Social 🚀",
        "likes": 0,
        "reposts": 0
    }
]


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>VIDEX Social</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            margin: 0;
            background: #0b0b0f;
            color: white;
            font-family: Arial, sans-serif;
        }

        header {
            padding: 18px;
            background: #15151d;
            border-bottom: 1px solid #292936;
            text-align: center;
        }

        header h1 {
            margin: 0;
            color: #b48cff;
        }

        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
        }

        .composer,
        .post {
            background: #15151d;
            border: 1px solid #292936;
            border-radius: 15px;
            padding: 18px;
            margin-bottom: 15px;
        }

        textarea {
            width: 100%;
            box-sizing: border-box;
            resize: none;
            min-height: 80px;
            background: #0b0b0f;
            color: white;
            border: 1px solid #333344;
            border-radius: 10px;
            padding: 12px;
            font-size: 15px;
        }

        button {
            margin-top: 10px;
            background: #8f5cff;
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 20px;
            cursor: pointer;
        }

        .actions {
            display: flex;
            gap: 20px;
            margin-top: 15px;
        }

        .actions button {
            background: transparent;
            padding: 5px;
        }

        .username {
            font-weight: bold;
            color: #b48cff;
        }

        .status {
            text-align: center;
            color: #7cff9b;
            margin-bottom: 20px;
        }
    </style>
</head>

<body>

<header>
    <h1>VIDEX</h1>
    <p>Connect. Share. Create.</p>
</header>

<div class="container">

    <div class="status">
        ● ONLINE
    </div>

    <div class="composer">
        <h3>Create a post</h3>

        <textarea id="postText"
                  placeholder="What's happening?"></textarea>

        <button onclick="createPost()">Post</button>
    </div>

    <div id="feed"></div>

</div>

<script>

async function loadPosts() {

    const response = await fetch("/api/posts");
    const posts = await response.json();

    const feed = document.getElementById("feed");

    feed.innerHTML = "";

    posts.slice().reverse().forEach(post => {

        const div = document.createElement("div");

        div.className = "post";

        div.innerHTML = `
            <div class="username">@${post.username}</div>

            <p>${post.text}</p>

            <div class="actions">

                <button onclick="likePost(${post.id})">
                    ❤️ ${post.likes}
                </button>

                <button onclick="repost(${post.id})">
                    🔁 ${post.reposts}
                </button>

            </div>
        `;

        feed.appendChild(div);
    });
}


async function createPost() {

    const text = document.getElementById("postText").value;

    if (!text.trim()) {
        alert("Write something first.");
        return;
    }

    await fetch("/api/posts", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            text: text
        })

    });

    document.getElementById("postText").value = "";

    loadPosts();
}


async function likePost(id) {

    await fetch(`/api/posts/${id}/like`, {
        method: "POST"
    });

    loadPosts();
}


async function repost(id) {

    await fetch(`/api/posts/${id}/repost`, {
        method: "POST"
    });

    loadPosts();
}


loadPosts();

</script>

</body>
</html>
"""


@app.route("/api/status")
def status():

    return jsonify({
        "app": "VIDEX",
        "status": "online",
        "version": "2.0"
    })


@app.route("/api/posts", methods=["GET"])
def get_posts():

    return jsonify(posts)


@app.route("/api/posts", methods=["POST"])
def create_post():

    data = request.get_json()

    text = data.get("text", "").strip()

    if not text:
        return jsonify({
            "error": "Post cannot be empty"
        }), 400

    new_post = {
        "id": len(posts) + 1,
        "username": "VIDEX_USER",
        "text": text,
        "likes": 0,
        "reposts": 0
    }

    posts.append(new_post)

    return jsonify(new_post), 201


@app.route("/api/posts/<int:post_id>/like", methods=["POST"])
def like_post(post_id):

    for post in posts:

        if post["id"] == post_id:

            post["likes"] += 1

            return jsonify(post)

    return jsonify({
        "error": "Post not found"
    }), 404


@app.route("/api/posts/<int:post_id>/repost", methods=["POST"])
def repost_post(post_id):

    for post in posts:

        if post["id"] == post_id:

            post["reposts"] += 1

            return jsonify(post)

    return jsonify({
        "error": "Post not found"
    }), 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
