<template>
  <div class="movie-form-wrapper">
    <h2 class="form-heading">Add a Movie</h2>

    <!-- Success alert -->
    <div v-if="successMessage" class="alert alert-success" role="alert">
      {{ successMessage }}
    </div>

    <!-- Error alerts — errors are plain strings from form_errors() -->
    <div v-if="errors.length > 0" class="alert alert-danger" role="alert">
      <ul class="error-list">
        <li v-for="(error, index) in errors" :key="index">
          {{ error }}
        </li>
      </ul>
    </div>

    <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data" novalidate>
      <div class="form-group">
        <label for="title" class="form-label">Movie Title</label>
        <input
          type="text"
          id="title"
          name="title"
          class="form-control"
          placeholder="Enter movie title"
        />
      </div>

      <div class="form-group">
        <label for="description" class="form-label">Description</label>
        <textarea
          id="description"
          name="description"
          class="form-control"
          rows="4"
          placeholder="Enter a brief description or summary of the movie"
        ></textarea>
      </div>

      <div class="form-group">
        <label for="poster" class="form-label">Movie Poster</label>
        <input
          type="file"
          id="poster"
          name="poster"
          class="form-control file-input"
          accept="image/*"
        />
      </div>

      <button type="submit" class="btn-submit">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const csrf_token = ref("");
const successMessage = ref("");
const errors = ref([]);

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => {
      console.error("Could not fetch CSRF token:", error);
    });
}

function saveMovie() {
  successMessage.value = "";
  errors.value = [];

  const movieForm = document.getElementById("movieForm");
  const formData = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": csrf_token.value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.errors) {
        // errors is a list of plain strings from form_errors()
        errors.value = data.errors;
      } else {
        successMessage.value = `"${data.title}" was successfully added!`;
        movieForm.reset();
        getCsrfToken();
      }
    })
    .catch((error) => {
      console.error("Request failed:", error);
    });
}

onMounted(() => {
  getCsrfToken();
});
</script>