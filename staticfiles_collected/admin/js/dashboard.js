document.addEventListener("DOMContentLoaded", function () {
    fetch("/admin/dashboard/")
        .then(response => response.json())
        .then(data => {
            document.getElementById("total-news").textContent = data.total_news;
            document.getElementById("total-users").textContent = data.total_users;
            document.getElementById("sentiment-stats").textContent = JSON.stringify(data.sentiment_counts);
        });
});
