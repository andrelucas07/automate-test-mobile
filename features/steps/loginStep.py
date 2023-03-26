from behave import given, when, then
from features.selenium_utils import *
from features.locators import *


@given(u'que o usuario tenha acesso ao app')
def open_app(context):
    context.driver.launch_app()


@when(u'fazer os primeiros passos')
def step_impl(context):
    multiple_clicks(context.driver, element=proximo_button, type_='xpath', quantity=2)
    click_element(context.driver, element=vamos_comecar_button, type_='xpath')
    click_element(context.driver, element=ja_tenho_conta_button, type_='xpath')


@when(u'inserir login e senha válidos')
def input_credentials(context):
    click_element(context.driver, element=input_email, type_='xpath')
    sleep(1)
    send_keys(context.driver, content='danielalocado@napista.com.br')
    click_element(context.driver, element=input_senha, type_='xpath')
    send_keys(context.driver, content='123qwe')
    click_element(context.driver, element=acessar_conta_button, type_='xpath')
    click_element(context.driver, element=biometria_button, type_='xpath')
    click_element(context.driver, element=group_button, type_='xpath')


@then(u'estara logado')
def step_impl(context):
    sleep(6)
    verificar_home = wait_for_find_element(context.driver, element=pagina_incial, type_='xpath')
    assert verificar_home
