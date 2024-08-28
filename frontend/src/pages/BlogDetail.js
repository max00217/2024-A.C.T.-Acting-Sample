import React, { useEffect, useState } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';

function BlogDetail() {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetch(`http://127.0.0.1:8080/posts/${id}`)
      .then(response => response.json())
      .then(data => setPost(data));
  }, [id]);

  const handleDelete = () => {
    const confirmDelete = window.confirm("이 글을 삭제하시겠습니까?");
    if (confirmDelete) {
      fetch(`http://127.0.0.1:8080/posts/${id}`, {
        method: 'DELETE',
      })
        .then(response => {
          if (response.ok) {
            alert("삭제 완료!");
            navigate('/blogs');
          } else {
            alert("Failed to delete post.");
          }
        });
    }
  };

  if (!post) return <div>Loading...</div>;

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
      <p><strong>Author:</strong> {post.author}</p>
      <p><strong>Created At:</strong> {post.time_posted}</p>
      <button onClick={() => navigate(`/edit/${id}`)}>Edit Post</button>
      <button onClick={handleDelete}>Delete Post</button>
    </div>
  );
}

export default BlogDetail;
