import codecs
codecs.register_error("strict", codecs.ignore_errors)

def render_email_text(
    template_plain,
    template_html,
    email_type_name,
    context_params,
    api_url
):
    """Render an e-mail message using our templates.

    :return: tuple of (text template, html template)
    """
    product = Product(
        api_url=api_url,
        type_name=email_type_name,
    )

    # Render the template according to the specification
    # within the product. We are being careful not to raise
    # any exceptions, so that the microservice
    # can fail gracefully.
    try:
        context_params['text_template'] = product.text
        context_params['html_template'] = product.html
        if 'api_url' in context_params:
            del context_params['api_url']
    except Exception:
        log.warning(
            '(render_email_text) Template for email type "%s" '%email_type_name
            + 'not found, using default
