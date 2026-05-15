#!/usr/bin/env python3
"""
KC Dumpster Phone Funnel Change
- Hide phone on all non-contact pages
- Convert phone CTAs to Contact Us / Get a Quote
- Add big Call Us Now button to top of contact.html
"""
import re
import os

SITE_DIR = "/Users/centralhq/.openclaw/workspace/clients/kansas-city-dumpsters/site"

# Pages to modify (hide phone)
NON_CONTACT_PAGES = [
    "index.html",
    "about.html",
    "faq.html",
    "how-it-works.html",
    "loading-rules.html",
    "pricing.html",
    "service-area.html",
    "service-residential.html",
]

def count_phone_occurrences(content):
    return len(re.findall(r'404.*?759.*?4361|4047594361|tel:\+14047594361', content, re.IGNORECASE))

def process_non_contact_page(filepath, filename):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_count = count_phone_occurrences(content)
    original = content

    # 1. NAV desktop: phone button -> Contact Us button
    # Pattern: <a href="tel:+14047594361" class="btn-orange px-5 py-2 rounded-lg text-sm ml-2">(404) 759-4361</a>
    content = re.sub(
        r'<a href="tel:\+14047594361" class="btn-orange px-5 py-2 rounded-lg text-sm ml-2">\(404\) 759-4361</a>',
        '<a href="contact.html" class="btn-orange px-5 py-2 rounded-lg text-sm ml-2">Get a Quote</a>',
        content
    )

    # 2. NAV mobile: Call (404)... button -> Contact Us button
    # Pattern: <a href="tel:+14047594361" class="btn-orange px-5 py-3 rounded-lg text-center font-heading font-bold text-sm mt-1">Call (404) 759-4361</a>
    content = re.sub(
        r'<a href="tel:\+14047594361" class="btn-orange px-5 py-3 rounded-lg text-center font-heading font-bold text-sm mt-1">Call \(404\) 759-4361</a>',
        '<a href="contact.html" class="btn-orange px-5 py-3 rounded-lg text-center font-heading font-bold text-sm mt-1">Contact Us</a>',
        content
    )

    # 3. HERO CTA on index.html: "Call (404) 759-4361" big button -> "Get a Quote"
    content = re.sub(
        r'<a href="tel:\+14047594361" class="btn-orange px-8 py-4 rounded-lg text-lg text-center">Call \(404\) 759-4361</a>',
        '<a href="contact.html" class="btn-orange px-8 py-4 rounded-lg text-lg text-center">Get a Quote</a>',
        content
    )

    # 4. FOOTER phone number links -> plain text with link to contact
    # Footer large phone link: <a href="tel:+14047594361" class="text-orange-400 font-heading font-700 text-lg hover:text-orange-300" ...>(404) 759-4361</a>
    content = re.sub(
        r'<a href="tel:\+14047594361" class="text-orange-400 font-heading font-700 text-lg hover:text-orange-300"[^>]*>\(404\) 759-4361</a>',
        '<a href="contact.html" class="text-orange-400 font-heading font-700 text-lg hover:text-orange-300" style="font-family:\'Montserrat\',sans-serif;font-weight:700;color:#FB923C;">Contact Us</a>',
        content
    )
    # Footer phone link (base size): <a href="tel:+14047594361" class="text-orange-400 font-heading font-700 text-base" style="...">(404) 759-4361</a>
    content = re.sub(
        r'<a href="tel:\+14047594361" class="text-orange-400 font-heading font-700 text-base"[^>]*>\(404\) 759-4361</a>',
        '<a href="contact.html" class="text-orange-400 font-heading font-700 text-base" style="font-family:\'Montserrat\',sans-serif;font-weight:700;color:#FB923C;">Contact Us</a>',
        content
    )

    # 5. STICKY CTA at bottom: Call (404)... -> Contact Us
    content = re.sub(
        r'(<div class="sticky-cta">.*?)<a href="tel:\+14047594361"([^>]*)>Call \(404\) 759-4361</a>',
        r'\1<a href="contact.html"\2>Contact Us</a>',
        content,
        flags=re.DOTALL
    )

    # 6. FINAL CTA section big white button with phone: -> Contact Us
    # <a href="tel:+14047594361" class="bg-white text-orange-700 ...>(404) 759-4361</a>
    content = re.sub(
        r'<a href="tel:\+14047594361" class="bg-white text-orange-700[^>]*>\(404\) 759-4361</a>',
        '<a href="contact.html" class="bg-white text-orange-700 font-heading font-700 px-10 py-4 rounded-lg text-lg hover:bg-orange-50 transition-colors" style="font-family:\'Montserrat\',sans-serif;font-weight:700;">Contact Us</a>',
        content
    )

    # 7. inline body text links: "...(404) 759-4361..." -> "...our contact page..."
    # Pattern: <a href="tel:+14047594361" class="text-brand-orange...>(404) 759-4361</a>
    content = re.sub(
        r'<a href="tel:\+14047594361" class="text-brand-orange[^>]*>\(404\) 759-4361</a>',
        '<a href="contact.html" class="text-brand-orange font-semibold hover:underline" style="color:#C44C0F;">contact us</a>',
        content
    )
    # about.html / faq.html pattern with inline style
    content = re.sub(
        r'<a href="tel:\+14047594361" class="text-brand-orange hover:underline"[^>]*>\(404\) 759-4361</a>',
        '<a href="contact.html" class="text-brand-orange hover:underline" style="color:#C44C0F;">contact us</a>',
        content
    )

    # 8. about.html hero CTA: "Call (404) 759-4361" button at top
    # <a href="tel:+14047594361" class="btn-orange px-8 py-3 rounded-lg text-sm">(404) 759-4361</a>
    content = re.sub(
        r'<a href="tel:\+14047594361" class="btn-orange px-8 py-3 rounded-lg text-sm">\(404\) 759-4361</a>',
        '<a href="contact.html" class="btn-orange px-8 py-3 rounded-lg text-sm">Get a Quote</a>',
        content
    )

    # 9. service-area.html big CTA button: <a href="tel:+14047594361" class="btn-orange px-10 py-4 rounded-lg text-lg text-center">(404) 759-4361</a>
    content = re.sub(
        r'<a href="tel:\+14047594361" class="btn-orange px-10 py-4 rounded-lg text-lg text-center">\(404\) 759-4361</a>',
        '<a href="contact.html" class="btn-orange px-10 py-4 rounded-lg text-lg text-center">Get a Quote</a>',
        content
    )

    # 10. service-residential.html CTA: same pattern
    content = re.sub(
        r'<a href="tel:\+14047594361" class="btn-orange px-10 py-4 rounded-lg text-lg text-center">\(404\) 759-4361</a>',
        '<a href="contact.html" class="btn-orange px-10 py-4 rounded-lg text-lg text-center">Get a Quote</a>',
        content
    )

    # 11. pricing.html "Call for Availability" buttons
    content = re.sub(
        r'<a href="tel:\+14047594361" class="btn-orange block text-center py-3 rounded-lg text-sm">Call for Availability</a>',
        '<a href="contact.html" class="btn-orange block text-center py-3 rounded-lg text-sm">Check Availability</a>',
        content
    )

    # 12. pricing.html "Still not sure?" inline text link
    content = re.sub(
        r'<a href="tel:\+14047594361" class="text-brand-orange font-semibold hover:underline"[^>]*>\(404\) 759-4361</a>',
        '<a href="contact.html" class="text-brand-orange font-semibold hover:underline" style="color:#C44C0F;">our contact page</a>',
        content
    )

    # 13. faq.html "Call us at (404)..." inline links
    # Already handled by pattern above but let's catch variations
    # Any remaining tel: href with visible phone numbers
    content = re.sub(
        r'<a href="tel:\+14047594361"([^>]*)>([^<]*\(404\)[^<]*)</a>',
        r'<a href="contact.html"\1>contact us</a>',
        content
    )
    # Any remaining tel: href with "Call (404)..." or just phone
    content = re.sub(
        r'<a href="tel:\+14047594361"([^>]*)>(Call\s*)?\(404\)[^<]*</a>',
        r'<a href="contact.html"\1>Contact Us</a>',
        content
    )

    # 14. how-it-works.html "Just call or text (404) 759-4361..." in body text
    # Replace the whole inline link
    content = re.sub(
        r'Just call or text <a href="tel:\+14047594361"[^>]*>\(404\) 759-4361</a>',
        'Just <a href="contact.html" class="text-brand-orange font-semibold hover:underline" style="color:#C44C0F;">contact us</a>',
        content
    )

    # 15. faq.html "Just call us and..." pattern
    content = re.sub(
        r'Call us at <a href="tel:\+14047594361"[^>]*>\(404\) 759-4361</a>',
        '<a href="contact.html" class="text-brand-orange hover:underline" style="color:#C44C0F;">Contact us</a>',
        content
    )
    content = re.sub(
        r'call us and[^<]*<a href="tel:\+14047594361"[^>]*>\(404\) 759-4361</a>',
        '<a href="contact.html" class="text-brand-orange hover:underline" style="color:#C44C0F;">contact us</a>',
        content
    )

    # 16. about.html special: "Call (404) 759-4361" footer link
    content = re.sub(
        r'<a href="tel:\+14047594361" class="text-white font-heading font-700 text-base"[^>]*>Call \(404\) 759-4361</a>',
        '<a href="contact.html" class="text-white font-heading font-700 text-base" style="font-family:\'Montserrat\',sans-serif;font-weight:700;">Contact Us</a>',
        content
    )

    # Catch-all: any remaining tel: links (should not break JSON-LD since those aren't anchor tags)
    # Replace any visible tel: anchor links
    content = re.sub(
        r'<a href="tel:\+14047594361"([^>]*)>([^<]+)</a>',
        r'<a href="contact.html"\1>Contact Us</a>',
        content
    )

    final_count = count_phone_occurrences(content)
    changed = content != original

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return original_count, final_count, changed


def process_contact_page():
    filepath = os.path.join(SITE_DIR, "contact.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add big Call Us Now button at top of contact body section, before existing Contact Details
    # Insert right after the page-hero section ends and the contact body section starts
    # Find the start of the contact body section
    
    call_now_block = '''
<!-- CALL NOW CTA -->
<section class="py-8 bg-orange-50 border-b border-orange-100">
  <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="text-gray-600 text-sm uppercase tracking-widest font-semibold mb-4">Fastest Way to Book</p>
    <a href="tel:4047594361" class="inline-block bg-brand-orange hover:bg-orange-700 text-white text-2xl md:text-3xl font-bold py-6 px-12 rounded-xl shadow-lg transition transform hover:scale-105" style="background:#E8611A;font-family:\'Montserrat\',sans-serif;font-weight:800;">
      Call Us Now
    </a>
    <p class="mt-4 text-xl font-semibold text-gray-700">(404) 759-4361</p>
    <p class="mt-2 text-sm text-gray-500">Tap to call on mobile. We answer 8am to 6pm.</p>
  </div>
</section>

'''

    # Insert before <!-- CONTACT BODY -->
    content = content.replace(
        '<!-- CONTACT BODY -->',
        call_now_block + '<!-- CONTACT BODY -->'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  contact.html: Added Call Us Now button at top")


def main():
    print("=== KC Dumpster Phone Funnel Change ===\n")
    results = {}

    for filename in NON_CONTACT_PAGES:
        filepath = os.path.join(SITE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  SKIP (not found): {filename}")
            continue
        
        before, after, changed = process_non_contact_page(filepath, filename)
        results[filename] = {"before": before, "after": after, "changed": changed}
        status = "MODIFIED" if changed else "NO CHANGE"
        print(f"  {filename}: {before} phone refs -> {after} remaining [{status}]")

    print()
    print("Processing contact.html...")
    process_contact_page()

    print()
    print("=== SUMMARY ===")
    for fn, r in results.items():
        print(f"  {fn}: {r['before']} -> {r['after']} phone refs")

    print()
    print("Done.")


if __name__ == "__main__":
    main()
