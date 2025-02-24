document.addEventListener("DOMContentLoaded", function () {
    const sidebar = `
        <div class="w-64 h-screen bg-gray-900 text-white p-4">
            <h2 class="text-xl font-bold mb-4">Admin Panel</h2>
            <ul>
                <li class="mb-2"><a href="/admin/dashboard">Dashboard</a></li>
                <li class="mb-2"><a href="/admin/news">Manage News</a></li>
                <li class="mb-2"><a href="/admin/users">Manage Users</a></li>
            </ul>
        </div>
    `;
    document.getElementById("admin-sidebar").innerHTML = sidebar;
});
