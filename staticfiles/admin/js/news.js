document.addEventListener("DOMContentLoaded", function () {
    fetch("/admin/news/")
        .then(response => response.json())
        .then(data => {
            let tableBody = "";
            data.news.forEach(news => {
                tableBody += `
                    <tr class="border">
                        <td class="border p-2">${news.title}</td>
                        <td class="border p-2">${news.department}</td>
                        <td class="border p-2">${news.sentiment}</td>
                    </tr>
                `;
            });
            document.getElementById("news-table-body").innerHTML = tableBody;
        });
});
