Feature: Login

  Scenario: Login com sucesso
    Given que o usuario tenha acesso ao app
    When fazer os primeiros passos
    And inserir login e senha válidos
    Then estara logado