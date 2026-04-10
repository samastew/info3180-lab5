<script setup>
import { ref } from "vue";

let message = ref("Your ultimate movie collection, powered by VueJS and Flask.")
</script>

<template>
  <div class="page-container">
    <div class="home-hero">
      <img alt="Vue logo" class="home-logo" src="@/assets/logo.svg" width="100" height="100" />
      <h1 class="home-title">CineVault</h1>
      <p class="home-subtitle">{{ message }}</p>
      <div class="home-actions">
        <RouterLink to="/movies/create" class="btn-primary">Add a Movie</RouterLink>
        <RouterLink to="/movies" class="btn-outline">Browse Movies</RouterLink>
      </div>
    </div>

    <div class="home-features">
      <div class="feature-card">
        <span class="feature-icon">🎬</span>
        <h3 class="feature-title">Add Movies</h3>
        <p class="feature-text">Upload your favourite movies with a title, description, and poster image.</p>
      </div>
      <div class="feature-card">
        <span class="feature-icon">🗂️</span>
        <h3 class="feature-title">Browse Collection</h3>
        <p class="feature-text">View your entire movie collection displayed in a clean, organised grid.</p>
      </div>
      <div class="feature-card">
        <span class="feature-icon">⭐</span>
        <h3 class="feature-title">Curate Your Library</h3>
        <p class="feature-text">Build your personal movie collection and share recommendations with friends.</p>
      </div>
    </div>
  </div>
</template>