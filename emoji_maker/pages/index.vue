<template>
<div>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">絵文字メーカー</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
  <div class="container">
    <br>
    <h2>絵文字をつけたい一文を入力してください</h2>
    <br>
    <b-form>
      <b-form-input
        id="inline-form-input-name"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="変換前のテキスト"
        v-model="src_txt"
      ></b-form-input>
      <b-button variant="success" @click="post({ src_txt })">送信</b-button>
    </b-form>
    <h1> {{ parse_txt }} </h1>
    </div>

</div>
</template>

<script>
import axios from 'axios';
export default {
  data () {
    return {
      src_txt: "",
      parse_txt: "",
    }
  },

  methods: {
    async post({src_txt}) {        
        // 取得先のURL
        //const url = 'http://192.168.2.226:5000/mecab/v1/parse-neologd';
        const url = 'https://3.239.235.148:8888';
        const response = await axios.post(url, {"sentence": src_txt},{ header : { 'Content-Type': 'application/json' }})
        if(response.data['result'])
          this.parse_txt = response.data['result']
        else
          this.parse_txt = "文をもう少し長くしてもう一度入力してください。"
      },
  }
}
</script>

<style>
.container {
  margin-top: 10px;
  display: inherit;
  justify-content: center;
  align-items: center;
  text-align: center;
}

h1 {
  margin-top: 20px;
}
form, input {
  text-align: center;
}

button {
  margin-top: 10px;
}

.title {
  font-family:
    'Quicksand',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
