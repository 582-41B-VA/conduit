<script lang="ts">
  import { goto } from "$app/navigation";

  const data = $state({
    username: "",
    email: "",
    password: "",
  });

  async function onsubmit(e: SubmitEvent): Promise<void> {
    e.preventDefault();
    // TODO: Handle errors
    const res = await fetch(`http://localhost:8000/api/users`, {
      method: "post",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ user: data }),
    });
    goto("/login");
  }
</script>

<div class="auth-page">
  <div class="container page">
    <div class="row">
      <div class="col-md-6 offset-md-3 col-xs-12">
        <h1 class="text-xs-center">Sign up</h1>
        <p class="text-xs-center">
          <a href="/login">Have an account?</a>
        </p>
        <!-- TODO: Handle error messages -->
        <ul class="error-messages">
          <li>That email is already taken</li>
        </ul>

        <form {onsubmit}>
          <fieldset class="form-group">
            <label>
              Username
              <input
                class="form-control form-control-lg"
                type="text"
                required
                bind:value={data.username}
              />
            </label>
          </fieldset>
          <fieldset class="form-group">
            <label>
              Email
              <input
                class="form-control form-control-lg"
                type="email"
                required
                bind:value={data.email}
              />
            </label>
          </fieldset>
          <fieldset class="form-group">
            <label>
              Password
              <input
                class="form-control form-control-lg"
                type="password"
                required
                bind:value={data.password}
              />
            </label>
          </fieldset>
          <button class="btn btn-lg btn-primary pull-xs-right">Sign up</button>
        </form>
      </div>
    </div>
  </div>
</div>
