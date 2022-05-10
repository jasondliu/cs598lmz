import selectnfpolicies
    record = selectnfpolicies.selectnfpolicies(pk)[0] # pk is int
    return render_to_response('record_detail.html', {'record': record })

def record_edit(request, pk):
    import selectnfpolicies
    record = selectnfpolicies.selectnfpolicies(pk)[0] # pk is int
    if request.method == "POST":
        form = RecordForm(request.POST)
        form.record = record # this is not a field in the form
        form.record_pk = pk # this is not a field in the form
        if form.is_valid():
            if 'delete' in request.POST:
                form.delete()
            else:
                form.save()
            return HttpResponseRedirect('/record/%s/' % pk)
    else:
        form = RecordForm(record)
        form.record = record # this is not a field in the form
        form.record_pk = pk # this is not a
