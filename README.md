<h1>Cargo Insurance instruction<p>

<h2>Установка и запуск приложения</h2>
<section><ul>
<li>Клонируйте репозиторий<br><code>git clone https://github.com/CHRNVpy/cargo_rates.git</code></li>
<li>Перейдите в директорию репозитория<br><code>cd cargo_rates</code></li>
<li>Создайте Docker контейнер<br><code>docker-compose up</code></li>
</ul>
</section>

<section>
<ul>После сборки контейнера сервер FastAPI запустится автоматически.<br>
    

<h2>API ENDPOINTS</h2>
<p>BASE URL: <code>https://0.0.0.0:8000</code></p>
<section>
  <h3>Добавление тарифов</h3>
  <p><strong>ENDPOINT:</strong> <code><strong>POST</strong> /api/rates/</code></p>
  <p><strong>Headers:</strong></p>
  <ul>
    <li><code>Content-Type:</code> application/json</li>
  </ul>
  <p>Example Request Body:</p>
  <img src="images/rates.png" alt="Rates Add Example Request">
</section>
<section>
  <h3>Получение cтоимости страхования</h3>
  <p><strong>ENDPOINT:</strong> <code><strong>GET</strong> /api/get_rates/</code></p>
  <p><strong>Headers:</strong></p>
  <ul>
    <li><code>Content-Type:</code> application/json</li>
  </ul>
  <p>Example Response:</p>
  <img src="images/get_rates_1.png" alt="Insurance Cost Example Response">
  <img src="images/get_rates_2.png" alt="Insurance Cost Example Response">
</section>
