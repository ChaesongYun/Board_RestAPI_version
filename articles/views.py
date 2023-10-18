from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시물 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시물 작성
    if request.method == 'POST':
        # data로 넘겨받은 데이터값은 유효성 검사를 위해 사용된다
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    # 특정 게시물 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 특정 게시물 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(
            {'delete': f'{article_pk}번 게시글이 삭제되었습니다'}, 
            status=status.HTTP_204_NO_CONTENT
        )
    
    # 특정 게시물 수정
    elif request.method == 'PUT':
        # 원래 건 첫번째 인자로, 수정값은 data인자로
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.sav()
            return Response(serializer.data)
        # serializer.data는 우리가 아는 딕셔너리 형태
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)