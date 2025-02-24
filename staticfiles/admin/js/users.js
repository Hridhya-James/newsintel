document.addEventListener("DOMContentLoaded", function () {
    fetch("/admin/users/")
        .then(response => response.json())
        .then(data => {
            let tableBody = "";
            data.users.forEach(user => {
                tableBody += `
                    <tr class="border">
                        <td class="border p-2">${user.username}</td>
                        <td class="border p-2">${user.email}</td>
                        <td class="border p-2">${user.role}</td>
                    </tr>
                `;
            });
            document.getElementById("users-table-body").innerHTML = tableBody;
        });
});
