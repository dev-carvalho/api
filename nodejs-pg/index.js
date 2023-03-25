//
// Código gerado pelo GTP em 24 / 03 / 2023
// 
// escreva um codigo comentado para  GRUP para postgres no padrão API REST em nodejs utilizando express
//

// As rotas incluem operações CRUD básicas para a tabela "usuarios", como consultar todos os usuários, consultar um usuário específico pelo ID, inserir um novo usuário, atualizar um usuário existente e remover um usuário existente.


// Importar as dependências necessárias
const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const Grup = require('grup');

// Configurar o aplicativo Express
const app = express();
app.use(bodyParser.json());

// Configurar o cliente de banco de dados do Postgres
const pool = new Pool({
  user: 'nome_de_usuario',
  host: 'localhost',
  database: 'nome_do_banco_de_dados',
  password: 'senha_do_banco_de_dados',
  port: 5432,
});

// Definir uma instância do Grup com a configuração do banco de dados
const grup = new Grup(pool);

// Definir as rotas para a API REST
app.get('/usuarios', async (req, res) => {
  // Consultar todos os usuários na tabela "usuarios"
  const usuarios = await grup.find('usuarios');
  res.json(usuarios);
});

app.get('/usuarios/:id', async (req, res) => {
  // Consultar um usuário específico pelo ID
  const usuario = await grup.findById('usuarios', req.params.id);
  res.json(usuario);
});

app.post('/usuarios', async (req, res) => {
  // Inserir um novo usuário na tabela "usuarios"
  const novoUsuario = await grup.insert('usuarios', req.body);
  res.json(novoUsuario);
});

app.put('/usuarios/:id', async (req, res) => {
  // Atualizar um usuário específico pelo ID
  const usuarioAtualizado = await grup.update('usuarios', req.params.id, req.body);
  res.json(usuarioAtualizado);
});

app.delete('/usuarios/:id', async (req, res) => {
  // Remover um usuário específico pelo ID
  const usuarioRemovido = await grup.remove('usuarios', req.params.id);
  res.json(usuarioRemovido);
});

// Iniciar o servidor na porta 3000
app.listen(3000, () => {
  console.log('Servidor iniciado na porta 3000.');
});
