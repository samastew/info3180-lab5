<template>
  <div class="page-container">
    <h2 class="page-heading">Movies</h2>

    <p v-if="movies.length === 0" class="no-movies-msg">
      No movies added yet. <RouterLink to="/movies/create">Add one!</RouterLink>
    </p>

    <div class="movies-grid">
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <img :src="movie.poster" :alt="movie.title" class="movie-poster" />
        <div class="movie-info">
          <h3 class="movie-title">{{ movie.title }}</h3>
          <p class="movie-description">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const movies = ref([]);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then((response) => response.json())
    .then((data) => {
      movies.value = data.movies;
    })
    .catch((error) => {
      console.error("Could not fetch movies:", error);
    });
}

onMounted(() => {
  fetchMovies();
});
</script>