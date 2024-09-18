# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ
from .forms import FAQForm

def faq_list(request):
    faqs = FAQ.objects.all()
    form = FAQForm()
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    return render(request, 'faq_list.html', {'faqs': faqs, 'form': form})

def edit_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm(instance=faq)
    return render(request, 'faq_list.html', {'form': form, 'edit_mode': True, 'faq_id': faq_id})

def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    faq.delete()
    return redirect('faq_list')

def view_schema(request):
    faqs = FAQ.objects.all()
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    for faq in faqs:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": faq.question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq.answer
            }
        })

    return render(request, 'schema_view.html', {'schema': schema})

# Create your views here.
