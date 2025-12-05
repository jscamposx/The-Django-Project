<h1>The Django Project Contents</h1>

<h3>Current Apps</h3>

<ul>
    <b>
    <li><a href="">accounts</a></li>
    <li><a href="">home</a></li>
    <li><a href="">post</a></li>
    <li><a href="">user_profile</a></li>
    </b>
</ul>

<hr>

<h3>Accounts contents</h3>

Accounts app handles the login, logout,signin procedures.
And mainly it also controls the Admin panel including User actions
<br>

Actions:

<ul>
    <b>
    <li>Account Deactivation/Activation</li>
    <li>Password Change</li>
    <li>Account Permissions</li>
    </b>
</ul>

These actions can be found in accounts/urls.py.

<hr>

<h3>Home contents</h3>

Home app handles displaying the home page with additional features such as,
the Top Post Filter and displaying Popular Posts.
The view functions (upvote,delete etc.) are copied from the Post app,
for the Popular Post page.

<hr>

<h3>Post contents</h3>

Post app handles alot of things and some things that are unrelated to the post app, these will be revamped in the future (ex. Contacts,Admin Panel,About page).
<br>

Post Handles:


<ul>
    <b>
    <li>Creation</li>
    <li>Deletion</li>
    <li>Updating</li>
    <li>Upvoting</li>
    <li>Viewership</li>
    <li>Detail</li>
    <li>Comments</li>
    <li>Admin Panel Actions (!)</li>
    </b>
</ul>

<br>
<b>Note:</b> this will be changed so admin panel has its own app.

<hr>

<h3>User_profile contents</h3>

The User_profile app is quite underdeveloped, and it only displays the profile page and allows the user to change its password and username.